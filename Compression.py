"""
Author: Sharat Vyas
Date: 12/11/2019

Explanation: This is a fairly simple implementation.
We are given a word/char list to encode with and a string we want
encoded/decoded. The first thing we do in either encoding/decoding
is to iterate thru our word/char list to get the distinct characters
that make up all the words/chars. We will hold this distinct list in a
new list called distinctCharList. Once done there are one of two things
can do.

If we are asked to encode a string, then we will iterate thru
the string and for each character, find the index of that character in
our distinctCharList and make the index of that character the INT
we use to encode the character. Example below....

wordList = <"ab","bab","dab","cab">
StringToEncode = "dabcab"

distinctCharList = <"a","b","d","c">
encodedString = <2,0,1,3,0,1>

Similarly, if we are asked to decode a string, we will first
get the distinctCharList. Once we have that list, we will
then iterate thru the encoded string and for each INT we iterate over,
we know that the integer we're using will represent the index of the char
in the distinctCharList. We then just get the char at that index in the list
and add it to our decoded string. Example below...

wordList = <"ab","bab","dab","cab">
StringToDecode = <2,0,1,3,0,1>

distinctCharList = <"a","b","d","c">
decodedString = "dabcab"

Runtime Analysis: Suppose we have 'm' words in our wordList that we use to
encode and decode. Let each of our m words have 'X^i' characters where i is
the index of the i-th word in wordList. Let N represent the length of the
string we want to encode/decode. We begin by iterating over our wordList
to get the distinct characters. We know that the iteration will run a total
of m times.The i-th word of our wordList can have X^i characters, and
we will iterate over each character in the i-th word. We will check if that
current character is contained in the distinctCharList of length 'c' and if
it doesn't we will add it. Let us assume that the longest word in wordList
is the k-th word, then we know that the runtime must be less than
O(m*X^k*c). The runtime for the actual compression and decompression
is identical. We iterate over the N characters/integers, in one case we get
the value of the index and in another case we get the index of the value.
In both cases, the calls are O(C) since we know that the length of '
distinctCharList is c. Then since we're iterating over all
n characters/integers, the call becomes O(n*c). In both the compression
and decompression methods we compute the distinctCharList then perform the
compression/decompression. As a result, we get a
total runtime for both methods of O(m*X^k*c) + O(n*c). Simplifying we get,
O(m*X^k*c). This shows us that the most costly component of the algorithm
is the part where we determine the distinctCharList which is used to
encode/decode

"""

from LList import LList


def StringCompression(subList, fullString):
    """

    :param subList: A list of words/characters used to encode/decode
    :param fullString: A string we want to encode into integers
    :return: Our encoded string
    """
    #Get the disctint individual characters from subList
    subCharList = ConvertWordListToCharList(subList)
    encodedString = LList()
    #Iterate thru the string we want to encode
    #Find the index of the current character in the subCharList
    #Make that index the encoded character and move on to next char
    for char in fullString:
        index = subCharList.index(char)
        encodedString.append(index)

    return encodedString


def StringDecompression(subList, encodedString):
    """
    This will take in our encoded string and will decode it to give us
    the original string
    :param subList: A list of words/characters used to encode/decode
    :param encodedString: Our StringCompression() encoded string
    :return: The original string we encoded
    """

    # Begin by converting the word-list/char-list to get the individual
    # characters it contains
    subCharList = ConvertWordListToCharList(subList)
    decodedWord = ""

    # Iterate thru each INT in the encoded string which represents
    # the index
    # of the target character in the subCharList, simply add that character
    for i in range(0, encodedString.__len__()):
        targetIndex = encodedString[i]
        targetChar = subCharList[targetIndex]
        decodedWord += targetChar
    return decodedWord


def ConvertWordListToCharList(inputList):
    """
    This will take in our wordList/charList that's used to encode/decode
    our string and will return the distinct individual characters of all
    those strings
    :param inputList: The list of individual words
    :return: The distinct characters contained in our list of
    words/characters
    """
    charList = LList()
    for word in inputList:
        for char in word:
            if not charList.__contains__(char):
                charList.append(char)

    return charList
