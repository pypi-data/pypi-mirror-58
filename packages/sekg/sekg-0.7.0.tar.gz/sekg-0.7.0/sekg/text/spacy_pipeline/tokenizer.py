# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: attenton
@Email: 18212010081@fudan.edu.cn
@Created: 2019/12/13
------------------------------------------
@Modify: 2019/12/13
------------------------------------------
@Description:
"""
import re

import spacy
from spacy.lang.char_classes import ALPHA, HYPHENS


class CustomizeSpacy:
    """
    apcy中的tokenizer主要原理分为五个部分，例外rules（也可以被称为tokenizer_exceptions）， 前缀prefix，后缀suffix，中缀infix，以及例外的正则匹配token_match
    修改以上任意一个都可以修改spacy中的tokenizer，实现自定义的tokenizer
    """
    @staticmethod
    def customize_tokenizer_split_single_lowcase_letter_and_period(nlp):
        """
        自定义的tokenzier，修改spacy中的exception，
        spacy中的tokenizer exception添加了{a.|b.|c.}等单个字母与句号连接的例外，这个可能导致分句出现错误，比如 1 < n < r. 出现在句尾。
        :param nlp:
        :return:
        """
        # prefix_re = spacy.util.compile_prefix_regex(nlp.Defaults.prefixes)
        # suffix_re = spacy.util.compile_suffix_regex(nlp.Defaults.suffixes)
        # infix_re = spacy.util.compile_infix_regex(nlp.Defaults.infixes)
        #
        # # remove all exceptions where a single letter is followed by a period (e.g. 'h.')
        exceptions = {k: v for k, v in dict(nlp.Defaults.tokenizer_exceptions).items() if
                      not (len(k) == 2 and k[1] == '.')}
        # new_tokenizer = Tokenizer(nlp.vocab, exceptions,
        #                           prefix_search=prefix_re.search,
        #                           suffix_search=suffix_re.search,
        #                           infix_finditer=infix_re.finditer,
        #                           token_match=nlp.tokenizer.token_match)
        #
        # nlp.tokenizer = new_tokenizer
        nlp.tokenizer.rules = exceptions

    @staticmethod
    def customize_tokenizer_merge_hyphen(nlp):
        """
        将连字符相连的合并为一个token， 如原来的fail-fast在tokenize之后会分成fail - fast三个，修改之后会全部合并为fail-fast这一个token
        实现方法： 删除infix中分离连字符的正则表达式
        :param nlp:
        :return:
        """
        _infixes = list(nlp.Defaults.infixes)
        _infixes.remove(r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),)
        infix_regex = spacy.util.compile_infix_regex(_infixes)
        nlp.tokenizer.infix_finditer = infix_regex.finditer

    @staticmethod
    def customize_tokenizer_api_name_recognition(nlp):
        """
        将句子中的api名字识别成一个token, 在生成tokenizer的函数后加上token.match
        TODO: 目前只是将中括号的合并了，由于token_match是在suffix、prefix之后执行，所以复杂的正则会被suffix、prefixoverride，所以目前还是用doc.retoeknizer()方法实现api_name的识别
        :param nlp:
        :return:
        """
        # re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
        _suffixes = list(nlp.Defaults.suffixes)
        _suffixes.remove("\]")
        suffixes_regex = spacy.util.compile_suffix_regex(_suffixes)
        nlp.tokenizer.suffix_search = suffixes_regex.search
        # api_name_match = re.compile("(\w+(\[[\w+-]+\])?\.)+\w+\(.*?\)", re.UNICODE).match
        # token_match = nlp.Defaults.token_match
        # print(token_match)
        # token_match.append(api_name_match)
        # nlp.tokenizer.token_match = api_name_match

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    CustomizeSpacy.customize_tokenizer_split_single_lowcase_letter_and_period(nlp)
    CustomizeSpacy.customize_tokenizer_merge_hyphen(nlp)
    CustomizeSpacy.customize_tokenizer_api_name_recognition(nlp)
    # sentence = 'java.lang.StringBuffer create StringBuffer'
    sentence = 'Suppose that a byte sequence of length n is written, where < n <= r. Up to the first srcs[offset].remaining() bytes of this sequence are written from buffer srcs[offset], up to the next srcs[offset+1].remaining() bytes are written from buffer srcs[offset+1], and so forth, until the entire byte sequence is written.'
    # sentence = "The elements in the array returned by the method executeBatch may be one of the following: A number greater than or equal to zero -- indicates that the command was processed successfully and is an update count giving the number of rows in the database that were affected by the command's execution"
    # sentence = "The maximum number of buffers-dke-dfs to be accessed 1 < n < r. So API must be non-negative and no larger than srcs.length - offset Returns long The number of bytes written, possibly zero"
    doc = nlp(sentence)
    # debug tokenizer
    tok_exp = nlp.tokenizer.explain(sentence)
    for t in tok_exp:
        print(t[1], "\t", t[0])
    for i in doc.sents:
        print(i)
        print([token.text for token in i])
        print([token.dep_ for token in i])
        print([token.tag_ for token in i])
        print([token.tag_ for token in i])
        print('\n')