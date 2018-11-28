import itertools
from collections import defaultdict
from operator import attrgetter
from os import path

import github
from gensim import corpora, models
from nltk.corpus import words, stopwords
from nltk.tokenize import RegexpTokenizer

# Some code  in this file has been borrowed from https://github.com/csurfer/gitsuggest/blob/master/gitsuggest/suggest.py
# I do not claim ownership of the code in the above link
# Appropriate modifications have been made at my descretion to suit the needs of my program

class Suggest:

    MAX_DESC_LEN = 300
    def __init__(self, username, password):
        self.g = github.Github(username, password)
        self.user = self.g.get_user()
        self.starred = list()
        self.following_starred = list()

        self.repo_to_use = self.__populate_repos()
        self.lda_model = None
        self.__construct_lda_model()

        self.suggested_repositories = None

    def __populate_repos(self):
        tempstarred = self.user.get_starred()
        if tempstarred==None:
            self.starred = list(self.user.get_repos())
            return
        length = len(list(tempstarred))
        if length >20:
             self.starred = tempstarred[:length]
        else:
            self.starred = tempstarred
            following_starred = self.user.get_following()
            add_to_starred = list()
            for following in following_starred:
                self.following_starred.extend(following.get_repos().get_page(0))

    def __construct_lda_model(self):
        # All repositories of interest.
        repos_of_interest = itertools.chain(
            self.starred,
            self.following_starred
        )

        # Extract descriptions out of repositories of interest.
        repo_descriptions = [repo.description for repo in repos_of_interest]
        repo_descriptions = list(set(repo_descriptions))
        # Get documents from the list of repositories
        repo_descriptions = filter(lambda x: x is not None and len(x) <= Suggest.MAX_DESC_LEN,repo_descriptions)
        #create tokenizer to remove all punctuation and non-latin characteres

        cleaned_tokens = self.__clean(repo_descriptions)

        # stop words are words such as 'an' and 'a' that a search engine will tend to avoid while parsing search terms
        # we want to also avoid using this in our repos to help find key words that we can act on
        # get words to ignore
        if not cleaned_tokens:
            cleaned_tokens = [["zkfgzkfgzkfgzkfgzkfgzkfg"]]

        dictionary = corpora.Dictionary(cleaned_tokens)
        corpus = [dictionary.doc2bow(text) for text in cleaned_tokens]

        # Generate LDA model
        self.lda_model = models.ldamodel.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=10)



    def __clean(self, repo_descriptions):
        tokenizer = RegexpTokenizer(r"[a-zA-Z]+")
        cleaned_doc_list = list()
        english_stopwords = stopwords.words("english")
        here = path.abspath(path.dirname(__file__))
        git_languages = []
        with open(path.join(here, "gitlang/languages.txt"), "r") as langauges:
            git_languages = [line.strip() for line in langauges]
        words_to_avoid = []
        with open(path.join(here, "gitlang/others.txt"), "r") as languages:
            words_to_avoid = [line.strip() for line in languages]
        # Compile all stop words together
        final_stopwords = set(itertools.chain(english_stopwords, git_languages, words_to_avoid))
        #
        words_dict = set(words.words())

        for doc in repo_descriptions:
            # Lowercase doc.
            lower = doc.lower()

            # Tokenize removing numbers and punctuation.
            tokens = tokenizer.tokenize(lower)

            # Include meaningful words.
            tokens = [tok for tok in tokens if tok in words_dict]

            # Remove stopwords.
            tokens = [tok for tok in tokens if tok not in final_stopwords]

            # Filter Nones if any are introduced.
            tokens = [tok for tok in tokens if tok is not None]

            cleaned_doc_list.append(tokens)
        return cleaned_doc_list


    def get_suggested(self):

        if self.suggested_repositories is None:
            # Procure repositories to suggest to user.
            repository_set = list()
            for term_count in range(5, 2, -1):
                query = self.__get_query_for_repos(term_count=term_count)
                repository_set.extend(self.__get_repos_for_query(query))

            # Remove repositories authenticated user is already interested in.
            catchy_repos = Suggest.minus(repository_set, self.starred)
        # Filter out repositories with too long descriptions. This is a
            # measure to weed out spammy repositories.
            filtered_repos = []

            if len(catchy_repos) > 0:
                for repo in catchy_repos:
                    if (repo is not None and repo.description is not None and len(repo.description) <= Suggest.MAX_DESC_LEN):
                        filtered_repos.append(repo)

            # Present the repositories, highly starred to not starred.
            filtered_repos = sorted(filtered_repos,key=attrgetter("stargazers_count"),reverse=True)

            self.suggested_repositories = Suggest.get_unique_repositories(filtered_repos)
            return self.suggested_repositories


    def __get_repos_for_query(self, query):
        return self.g.search_repositories(query, "stars", "desc").get_page(0)

    def __get_query_for_repos(self, term_count=5):
        repo_query_terms = list()
        for term in self.lda_model.get_topic_terms(0, topn=term_count):
            repo_query_terms.append(self.lda_model.id2word[term[0]])
        return " ".join(repo_query_terms)

    @staticmethod
    def get_unique_repositories(repo_list):
        """Method to create unique list of repositories from the list of
        repositories given.
        :param repo_list: List of repositories which might contain duplicates.
        :return: List of repositories with no duplicate in them.
        """
        unique_list = list()
        included = defaultdict(lambda: False)
        for repo in repo_list:
            if not included[repo.full_name]:
                unique_list.append(repo)
                included[repo.full_name] = True
        return unique_list

    @staticmethod
    def minus(repo_list_a, repo_list_b):
        """Method to create a list of repositories such that the repository
        belongs to repo list a but not repo list b.
        In an ideal scenario we should be able to do this by set(a) - set(b)
        but as GithubRepositories have shown that set() on them is not reliable
        resort to this until it is all sorted out.
        :param repo_list_a: List of repositories.
        :param repo_list_b: List of repositories.
        """
        included = defaultdict(lambda: False)

        for repo in repo_list_b:
            included[repo.full_name] = True

        a_minus_b = list()
        for repo in repo_list_a:
            if not included[repo.full_name]:
                included[repo.full_name] = True
                a_minus_b.append(repo)
        return a_minus_b
