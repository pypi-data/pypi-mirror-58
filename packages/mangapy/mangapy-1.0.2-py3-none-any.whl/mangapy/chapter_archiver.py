import re
import requests
from functools import partial
from tqdm import tqdm
from PIL import Image
from urllib.parse import urlparse
from mangapy.mangarepository import Chapter, Page
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


class ChapterArchiver(object):
    session = requests.Session()

    def __init__(self, path: str, max_workers=1):
        self.max_workers = max_workers
        self.path = Path(path).expanduser()
        self.images_path = self.path.joinpath('images')
        self.pdf_path = self.path.joinpath('pdf')

    def archive(self, chapter: Chapter):
        chapter_images_path = self.images_path.joinpath(str(chapter.number))
        chapter_images_path.mkdir(parents=True, exist_ok=True)
        pages = chapter.pages()
        description = ('Chapter {0}'.format(str(chapter.number)))
        func = partial(self._save_image, chapter_images_path)  # currying

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            list(tqdm(executor.map(func, pages), total=len(pages), desc=description, unit='pages', ncols=100))

        self.pdf_path.mkdir(parents=True, exist_ok=True)
        chapter_pdf_file_path = self.pdf_path.joinpath(str(chapter.number) + '.pdf')
        self._create_chapter_pdf(chapter_images_path, chapter_pdf_file_path)

    def _fetch_image(self, url: str):
        response = self.session.get(url, verify=False)
        if response.status_code != 200:
            return None
        return response.content

    def _save_image(self, image_path: Path, page: Page):
        file_name = str(page.number)
        image_url = page.url
        file_ext = urlparse(image_url).path.split('.')[-1]
        if image_url.startswith('//'):
            image_url = 'http:' + image_url

        data = self._fetch_image(image_url)

        if data is None:
            return

        file_path = image_path.joinpath(file_name + '.' + file_ext)
        output = open(file_path, "wb")
        output.write(data)
        output.close()

    def _create_chapter_pdf(self, chapter_images_path: Path, pdf_path: Path):
        file_list = list(chapter_images_path.glob('**/*'))  # we don't care of their ext
        chapter_images_path = list(map(lambda path: str(path.absolute()), file_list))
        images_path = natural_sort(chapter_images_path)

        images = []
        for path in images_path:
            image = Image.open(path)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            images.append(image)

        images_count = len(images)
        if images_count <= 0:
            return
        elif images_count == 1:
            first_image = images.pop(0)
            first_image.save(pdf_path, "PDF", resolution=100.0, save_all=True)
        else:
            first_image = images.pop(0)
            first_image.save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images)


def natural_sort(list):
    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split('([0-9]+)', key)]

    return sorted(list, key=alphanum_key)
