class Article:
    
    all =[]
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if (isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, 'title')):
            self._title = new_title
        else:
            raise Exception ('wrong article title')
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if(isinstance(new_author, Author)):
            self._author = new_author
        else:
            print('wrong author name')
            
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, new_magazine):
        if(isinstance(new_magazine, Magazine)):
            self._magazine = new_magazine
        else:
            print('wrong magazine name')
            
    def __repr__(self):
        return f'<Article title = {self.title} magazine = {self.magazine} author = {self.author} />'
    
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(magazine=magazine, title=title, author=self)

    def topic_areas(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return list(set([mag.category for mag in self.magazines()]))
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if(isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, 'name')):
            self._name = new_name
        else:
            print('wrong name')
            
    def __repr__(self):
        return f'Author: {self.name}'

class Magazine:
    
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if(len(self.articles()) == 0):
            return None
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        articles = self.articles()
        
        if not articles:
            return None
        
        get_authors = set(article.author for article in articles)
        
        cont_auth = []
        
        for author in get_authors:
            count = sum(1 for article in articles if article.author == author)
            if count >= 2:
                cont_auth.append(author)
                
        if(cont_auth == []):
            return None
        return cont_auth
    
    @classmethod
    def top_publisher(cls):
        best_mag = None
        best_mag_article_count = 0
        for mag in Magazine.all:
            if(len(mag.aarticles()) > best_mag_article_count):
                best_mag_article_count = len(mag.articles())
                best_mag = mag
        return best_mag
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if(isinstance(new_name, str) and 2 <= len(new_name)<= 16):
            self._name = new_name
        else:
            print('wrong name')
            
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        if(isinstance(new_category, str) and 0 < len(new_category)):
            self._category = new_category
        else:
            print('wrong category')
            
    def __repr__(self):
        return f'<Magazine name={self.name} category={self.category}/>'