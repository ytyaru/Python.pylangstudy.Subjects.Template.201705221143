#!python3
#encoding: utf-8
import urllib.parse
import htmlstr.HeaderNavi
import htmlstr.NextPrevNavi
import htmlstr.HtmlWrapper
class Template_Navi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()
        self.__nav_head = htmlstr.HeaderNavi.HeaderNavi()
        self.__nav_next = htmlstr.NextPrevNavi.NextPrevNavi()
    
    def WrapNavi(self, breadcrumbs_data, metanavi_data, nextprevnavi_data):
        nav_head_str = self.__nav_head.CreateHtml(breadcrumbs_data, metanavi_data)
        nav_next_str = self.__nav_next.CreateHtml(nextprevnavi_data['prev'], nextprevnavi_data['next'])
        return nav_head_str + '\n\n' + nav_next_str
    
    def __CreateNextPrevNavi(self, nextprevnavi_data):
        if 'directional_icon_type' in nextprevnavi_data:
            return htmlstr.NextPrevNavi.NextPrevNavi(nextprevnavi_data['directional_icon_type'])
        else:
            return htmlstr.NextPrevNavi.NextPrevNavi()


if __name__ == '__main__':
    breadcrumbs_data = {
        'directional_icon_type': 'FontAwesome',
        'datas': [
            {'text': '孫', 'href': 'http://2'},
            {'text': '子', 'href': 'http://1'},
            {'text': '親', 'href': 'http://0'}],
        'is_child_first': True
    }
    metanavi_data = {
        'pydoc': {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
        'env': {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
        'github': {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'}
    }
    nextprevnavi_data = {
        'directional_icon_type': 'FontAwesome',
        'prev': {'text': '前のページ', 'href': 'http://prev'},
        'next': {'text': '次のページ', 'href': 'http://next'}
    }
    print(Template_Navi().CreateHtml(breadcrumbs_data, metanavi_data, nextprevnavi_data))
