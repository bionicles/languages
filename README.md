# Languages

## A python function to load word, character lists for a bunch of languages


## Install

```
git clone https://github.com/bionicles/languages && cd languages && unzip languages.zip && python languages.py
```

You may need to install fonts and change the font in your terminal to get this to display properly. 

FWIW, most everything prints OK on my rig now (june 2020), here 
are my fonts in VS Code:
```
"editor.fontFamily": "'Noto Mono', 'Noto Color Emoji', 'NotoSansCJK-Regular'",
"terminal.integrated.fontFamily": "'unifont','Noto Mono', 'Noto Color Emoji', 'NotoSansCJK-Regular'",
```

## Use

print the languages:
```bash
python languages.py 
```

import them and use them for NLP or apps
```py
from languages import load_languages

languages = load_languages()

# languages is a dict with [language]['words'] and [language]['chars']
# language keys are ISO-639-3 three-letter codes

swahili = languages['swa']
russian_words = languages['rus']['words']
chinese_chars = languages['cmn']['chars']
```

## Languages

1. kor, korean
1. hin, hindi
1. ben, bengali
1. swa, swahili
1. gle, irish
1. urd, urdu
1. pus, pashto / pushto
1. fas, farsi / persian
1. arb, arabic
1. lat, latin
1. fra, french
1. cmn, mandarin chinese
1. rus, russian
1. spa, spanish
1. ell, greek
1. heb, hebrew
1. deu, german
1. als, albanian
1. eng, english
1. bul, bulgarian
1. cat, catalan
1. dan, danish
1. eus, basque
1. fin, finnish
1. glg, galician
1. hrv, croatian
1. ind, indonesian
1. ita, italian
1. jpn, japanese
1. nld, dutch
1. nno, norwegian nynorsk
1. nob, norwegian bokmal
1. pol, polish
1. por, portuguese
1. qcn, chinese wordnet
1. slv, slovenian
1. swe, swedish
1. tha, thai
1. zsm, malay


## Layout

'languages' is a dictionary of language dictionaries; each language dictionary has 'words' and 'chars'

The keys are [ISO-639 3-letter language codes](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Languages/List_of_ISO_639-3_language_codes_(2019))


## Contribute

I'm keeping this intentionally simple as **** for now, but I welcome forks, pull requests, comments. 

## Ideas:
-We could add code to regenerate the json (I hacked this in the Python REPL) 
-we could add functions to merge the languages into a mecha-list. 
-we could improve the deduplication
-we could define the words
-we could add emoji
-json might be too annoying and we could switch to csv
-we could add this to NLTK


## License / Sources

MIT from my end

Many others contributed data for the project:

German came from ubuntu /usr/share/dict/ogerman|ngerman (installed through the "Language Support" program)

Russian came from [YARN - Yet Another RussNet](https://russianword.net/en/)

YARN: Spinning-in-Progress / P. Braslavski, D. Ustalov, M. Mukhin, Y. Kiselev // Proceedings of the Eight Global Wordnet Conference. — Bucharest, Romania, 2016 — P. 58–65 (PDF)

Latin is from [William Whitaker](https://en.wikipedia.org/wiki/William_Whitaker%27s_Words)

Urdu is from the [UrduHack](https://github.com/urduhack) team on github

Irish is from [Michal Boleslav Měchura](http://www.lexiconista.com/)

Swahili is from [Elastic's hunspell](https://github.com/elastic/hunspell)

Korean is from [Jiseong Kim at KAIST](http://wordnet.kaist.ac.kr/wordnet/contents_en.php)

Pashto came from [Mohammad Badar Hashimi](https://github.com/mohbadar)

Bengali is from [Minhas Kamal](https://github.com/MinhasKamal)

Hindi came from [Aleksander Eskilson](https://github.com/bdrillard)

most of the dataset came from [Open Multilingual Wordnet](http://compling.hss.ntu.edu.sg/omw/) 

References from Open Multilingual Wordnet:

als Ervin Ruci (2008)

On the current state of Albanet and related applications, Technical Report, University of Vlora

all Francis Bond and Kyonghee Paik (2012)

A survey of wordnets and their licenses In Proceedings of the 6th Global WordNet Conference (GWC 2012). Matsue. 64–71

Francis Bond and Ryan Foster (2013) Linking and extending an open multilingual wordnet. In 51st Annual Meeting of the Association for Computational Linguistics: ACL-2013. Sofia. 1352–1362

arb Black W., Elkateb S., Rodriguez H., Alkhalifa M., Vossen P., Pease A., Bertran M., Fellbaum C., (2006)

The Arabic WordNet Project, Proceedings of LREC 2006

Lahsen Abouenour, Karim Bouzoubaa, Paolo Rosso (2013)
On the evaluation and improvement of {Arabic} WordNet coverage and usability, Language Resources and Evaluation 47(3) pp 891–917

bul Simov, Kiril and Osenova, Petya (2010)

Constructing of an Ontology-based Lexicon for Bulgarian, Proceedings of LREC 2010

cat, glg, spa, Aitor Gonzalez-Agirre, Egoitz Laparra and German Rigau (2012)

Multilingual Central Repository version 3.0: upgrading a very large lexical knowledge base. In Proceedings of the 6th Global WordNet Conference (GWC 2012) Matsue, Japan.

eus Elisabete Pociello, Eneko Agirre and Izaskun ldezabal (2010)

Methodology and construction of the Basque WordNet Language Resources and Evaluation Springer Netherlands 45(2) pp 121–142

core Boyd-Graber, J., Fellbaum, C., Osherson, D., and Schapire, R. (2006)

Adding dense, weighted connections to WordNet. In: Proceedings of the Third Global WordNet Meeting, Jeju Island, Korea, January 2006

cmn Shan Wang and Francis Bond (2013)

Building the Chinese Open Wordnet (COW): Starting from Core Synsets. In Proceedings of the 11th Workshop on Asian Language Resources, a Workshop of The 6th International Joint Conference on Natural Language Processing (IJCNLP-6). Nagoya, Japan. pp.10–18.

qcn Huang, C.-R., Hsieh, S.-K., Hong, J.-F., Chen, Y.-Z., Su, I.-L., Chen, Y.-X., and Huang, S.-W. (2010).

Chinese wordnet: Design and implementation of a cross-lingual knowledge processing infrastructure. In Journal of Chinese Information Processing. 24(2) pp 14–23. (in Chinese)

dan Pedersen, B. S., Nimb, S., Asmussen, J., Sørensen, N. H., Trap-Jensen, L. and Lorentzen, H. (2009)

DanNet -- the challenge of compiling a WordNet for Danish by reusing a monolingual dictionary Language Resources and EvaluationVolume 43:3 pp. 269-299

eng Christiane Fellbaum. (ed.) (1998)

WordNet: An Electronic Lexical Database, MIT Press

ell Sofia Stamou, Goran Nenadic and Dimitris Christodoulakis (2004)

Exploring Balkanet Shared Ontology for Multilingual Conceptual Indexing, Proceedings of LREC 2004

fra Benoit Sagot and Darla Fišer (2008)

Building a free French wordnet from multilingual resources, E. L. R. A. (ELRA) (ed.), Proceedings of the Sixth International Language Resources and Evaluation (LREC’08), Marrakech, Morocco

heb Noam Ordan and Shuly Wintner (2007)

Hebrew WordNet: a test case of aligning lexical databases across languages. International Journal of Translation 19(1):39–58, 2007

hrv Oliver A., Šojat, K., Srebačić, M. (2015)

Automatic Expansion of Croatian Wordnet In Proceedings of the 29th CALS international conference: Applied Linguistic Research and Methodology Zadar (Croatia)

Raffaelli, Ida; Bekavac, Božo; Agić, Željko; Tadić, Marko. (2008)

Building Croatian WordNet. In Proceedings of the Fourth Global WordNet Conference pp349-359

ita Emanuele Pianta, Luisa Bentivogli and Christian Girardi. (2002)

MultiWordNet: Developing an Aligned Multilingual Database. In Proceedings of the First International Conference on Global WordNet, Mysore, India, January 21-25, 2002, pp. 293-302.

Antonio Toral, Stefania Bracal, Monica Monachini and Claudia Soria (2010)

Rejuvenating the Italian WordNet: upgrading, standardising, extending In Proceedings of the 5th International Conference of the Global WordNet Association (GWC-2010) Mumbai

ind,zsm Nurril Hirfana Mohamed Noor, Suerya Sapuan and Francis Bond (2011)

Creating the open Wordnet Bahasa In Proceedings of the 25th Pacific Asia Conference on Language, Information and Computation (PACLIC 25) pages 258–267. Singapore

jpn Hitoshi Isahara, Francis Bond, Kiyotaka Uchimoto, Masao Utiyama and Kyoko Kanzaki (2008)

Development of Japanese WordNet. In LREC-2008, Marrakech.

fas Montazery, Mortaza and Heshaam Faili (2010)

Automatic Persian WordNet Construction the 23rd International conference on computational linguistics pp. 846–850

fin Lindén K., Carlson. L., (2010)

FinnWordNet — WordNet påfinska via översättning,LexicoNordica — Nordic Journal of Lexicography, 17 pp 119–140

lit Garabík, Radovan and Pileckytė, Indrė (2013)

From Multilingual Dictionary to Lithuanian WordNet. In: Natural Language Processing, Corpus Linguistics, E-Learning. Ed. Katarína Gajdošová — Adriána Žáková. Lüdenscheid: RAM-Verlag, pp. 74–80.

sentiwn Baccianella, Andrea Esuli Stefano and Sebastiani, Fabrizio, (2010)

SentiWordNet 3.0: An Enhanced Lexical Resource for Sentiment Analysis and Opinion Mining., Proceedings of the Seventh conference on International Language Resources and Evaluation (LREC'10) , Valletta, Malta, 2010

ml-senticon Cruz, Fermín L., José A. Troyano, Beatriz Pontes, F. Javier Ortega, (2014)
Building layered, multilingual sentiment lexicons at synset and lemma levels, Expert Systems with Applications , 2014

mapp Jordi Daudé, Lluís Padró and German Rigau (2000)

Mapping WordNets Using Structural Information. 38th Annual Meeting of the Association for Computational Linguistics (ACL'2000), Hong Kong

nld Marten Postma, Emiel van Miltenburg, Roxane Segers, Anneleen Schoen and Piek Vossen (2016)

Open Dutch WordNet, Proceedings of the Eight Global Wordnet Conference Bucharest, Romania.

nno,nob Fjeld, Ruth Vatvedt and Nygaard, Lars (2009)

NorNet - a monolingual wordnet of modern Norwegian In Proceedings of the NODALIDA 2009 workshop WordNets and other Lexical Semantic Resources — between Lexical Semantics, Lexicography, Terminology and Formal Ontologies. pages 13–16. Estonia

pol Maciej Piasecki, Stanisław Szpakowicz and Bartosz Broda. (2009)

A Wordnet from the Ground Up. Wroclaw: Oficyna Wydawnicza Politechniki Wroclawskiej, Poland.

por Valeria de Paiva and Alexandre Rademaker (2012)

Revisiting a Brazilian wordnet. In Proceedings of Global Wordnet Conference, Matsue. Global Wordnet Association. (also with Gerard de Melo's contribution)

ron Tufiș, Dan, Ion, Radu, Bozianu, Luigi, Ceaușu, Alexandru and Ștefănescu, Dan. (2008)

Romanian Wordnet: Current State, New Applications and Prospects. In Proceedings of the 4th Global WordNet Conference, GWC-2008 Eds. Tanacs, Attila, Csendes, Dora, Vincze, Veronika, Fellbaum, Christiane and Vossen, Piek. Szeged, Hungary, pp. 441–452

slv Fišer, Darja, and Novak, Jernej, and Eejavec, Tomaž (2012)

sloWNet 3.0: development, extension and cleaning. In Proceedings of the 6th International Global Wordnet Conference (GWC 2012).. The Global WordNet Association, pp. 113-117

sumo Adam Pease (2011)

Ontology: A Practical Guide. Articulate Software Press, Angwin, CA. ISBN 978-1-889455-10-5.

sumo Niles, I and Adam Pease (2001)

Toward a Standard Upper Ontology. In Proceedings of the 2nd International Conference on Formal Ontology in Information Systems (FOIS-2001), Chris Welty and Barry Smith, eds.

swe Borin, Lars and Forsberg, Markus and Lönngren, Lennart (2013)

SALDO: a touch of yin to WordNet's yang. Language Resources and Evaluation 47(4) pp 1191–1211 tempo Gaël Dias, Mohammed Hasanuzzaman, Stéphane Ferrari, Yann Mathet (2014)

TempoWordNet for Sentence Time Tagging. Proceedings of the Companion Publication of the 23rd International Conference on World Wide Web Companion pages 833–838, Switzerland

tha Thoongsup S., Charoenporn T., Robkop K., Sinthurahat T., Mokarat C., Sornlertlamvanich V., Isahara H. (2009)

Thai Wordnet Construction Proceedings of The 7th Workshop on Asian Language Resources (ALR7), Joint conference of the 47th Annual Meeting of the Association for Computational Linguistics (ACL) and the 4th International Joint Conference on Natural Language Processing (IJCNLP) Suntec, Singapore

Language codes linked to Lewis, M. Paul (ed.), 2009. Ethnologue: Languages of the World, Sixteenth edition. Dallas, Tex.: SIL International. Online version: http://www.ethnologue.com/
