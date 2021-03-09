import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass


class TextComparer():
    
    def __init__(self, url_list):
        self.url_list = url_list
        self._filenames = []
        self.num = 0

    def __iter__(self):
        return self
    
    def __next__(self): 
        if (self.num <= len(self._filenames)):
            num = self.num
            self.num += 1
            return self._filenames[num]
        else:
            self.num = 0
            raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url
    
    def download(self, url, filename):
            r = requests.get(url)
            if not (r.ok):
                raise NotFoundException()

            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)

    def multi_download(self):
        workers = 5
        folder = 'modules/week6/textfiles/'
    
        for index, val in enumerate(self.url_list):
            s = folder + "file" + str(index) + ".txt"
            self._filenames.append(s) 
           
        with ThreadPoolExecutor(workers) as ex:
            ex.map(self.download, self.url_list, self._filenames)
    

    def avg_vowels(self, text):
        try:
            count = 0
            file = open(text, 'r')
            text_file = file.read()
            vowel = set("aeiou")
            word_list = text_file.split(" ")
            for s in text_file.lower():
                if (s in vowel):
                    count += 1
            file.close()
            return round(count / len(word_list), 2)
        except Exception:
            print("No file found...")


    def hardest_read(self):
        workers = multiprocessing.cpu_count()
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, self._filenames)

        results = dict(zip(self._filenames, list(res)))
        return max(results, key=results.get)

    def bar_data(self):
        workers = multiprocessing.cpu_count()
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, self._filenames)

        results = dict(zip(self._filenames, list(res)))
        return dict(sorted(results.items(), key=lambda item: item[1]))
