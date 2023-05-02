from content_block_functions import create_content_block
from answer_option_functions import *
from nextLogic_functions import *

def create_beginning(id, version, journey_key, information):
    beginning = '''
{
  "id": "%s",
  "key": "%s",
  "order": 10,
  "mainImageName": "red_main.png",
  "mainImageLongName": "red_main.png",
  "topicIconImageName": "core.svg",
  "mainImageLockedLongName": "red_main.png",
  "backgroundImageName": "red_background.jpeg",
  "sessionImageName": "red_session.png",
  "published": true,
  "publishedEN": false,
  "feedbackLink": null,
  "version": %s,
  "type": "SHORT_TRIP",
  "compulsoryOrder": false,
  "topicId": null,
  "backgroundImageLockedName": "dark_main.png",
  "translations": [
    {
      "id": "%s-DE",
      "language": "DE",
      "title": "%s",
      "subTitle": "",
      "description": null
    },
    {
      "id": "%s-EN",
      "language": "EN",
      "title": "Englisch",
      "subTitle": "",
      "description": null
    }
  ],
  "content": [
    {
      "id": "%s-cont",
      "order": 2,
      "type": "PARAGRAPH",
      "imageName": null,
      "translations": [
        {
          "id": "%s-cont-DE",
          "language": "DE",
          "title": null,
          "text": "%s"
        },
        {
          "id": "%s-cont-EN",
          "language": "EN",
          "title": null,
          "text": "Englisch"
        }
      ]
    },
    {
      "id": "%s-s1",
      "order": 4,
      "type": "SESSION_TITLE",
      "imageName": null,
      "translations": [
        {
          "id": "%s-s1-DE",
          "language": "DE",
          "title": null,
          "text": "%s"
        },
        {
          "id": "%s-s1-EN",
          "language": "EN",
          "title": null,
          "text": "Englisch"
        }
      ]
    }
  ],
  "sessions": [
    {
      "id": "%s-1",
      "order": 1,
      "durationMin": %s,
      "durationMax": %s,
      "translations": [
        {
          "id": "%s-1-DE",
          "language": "DE",
          "title": "%s"
        },
        {
          "id": "%s-1-EN",
          "language": "EN",
          "title": "Englisch"
        }
      ],
      "questions": [
        ''' % (id+version, journey_key, version, id+version, information[0], id+version, id+version, id+version, information[1], id+version, id+version, id+version, information[3], id+version, id+version, information[5], information[6], id+version, information[2], id+version)
    return beginning

def get_content_length(contents):
    count_A = contents.count('A')
    count_I = contents.count('I')
    length = len(contents)+count_A+count_I+2
    return length

def create_question(question, type, id_base, count, write_beginning, contents, answer_options, next_logics, next_logic_type, texts, id_base_next_question):
    # DICTIONARY
    return {
        "CONTENT": ''' 
        {
          "id": "%s",
          "type": "CONTENT",
          "number": null,
          "minNumber": null,
          "maxNumber": null,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": null,
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s
          ],
          "nextLogic": {
            "id": "%s",
            "type": "%s",
            "count": null,
            "nextQuestionId": "%s",
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
            %s
            ],
            "refAdaptions": []
          }
        },''' % (id_base, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base, texts[0], id_base, create_content_block(id_base, 2, contents, texts), id_base, next_logic_type, id_base_next_question, create_nextLogic_options(id_base, get_content_length(contents), next_logics, next_logic_type)),
        "OPTION_QUESTION": '''
        {
          "id": "%s",
          "type": "OPTION_QUESTION",
          "number": null,
          "minNumber": null,
          "maxNumber": null,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": "",
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s
            ,{
              "id": "%s-%s",
              "type": "ANSWER_OPTION",
              "required": true,
              "showHidden": null,
              "order": %s,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [],
              "answerOptions": [
                {
                  "id": "%s-%s-1",
                  "order": 1,
                  "number": null,
                  "type": "BUTTON",
                  "imageName": null,
                  "hidden": null,
                  "escapeOption": null,
                  "sliderType": null,
                  "negative": null,
                  "unselectOthers": null,
                  "booleanHelper": null,
                  "refQuestionAnswerOptionId": null,
                  "secondRefQuestionAnswerOptionId": null,
                  "questionLoopCycleId": null,
                  "translations": [
                    {
                      "id": "%s-%s-1-DE",
                      "language": "DE",
                      "title": null,
                      "text": "Ja",
                      "description": ""
                    },
                    {
                      "id": "%s-%s-1-EN",
                      "language": "EN",
                      "title": "",
                      "text": "Englisch",
                      "description": ""
                    }
                  ]
                },
                {
                  "id": "%s-%s-2",
                  "order": 2,
                  "number": null,
                  "type": "BUTTON",
                  "imageName": null,
                  "hidden": null,
                  "escapeOption": null,
                  "sliderType": null,
                  "negative": null,
                  "unselectOthers": null,
                  "booleanHelper": null,
                  "refQuestionAnswerOptionId": null,
                  "secondRefQuestionAnswerOptionId": null,
                  "questionLoopCycleId": null,
                  "translations": [
                    {
                      "id": "%s-%s-2-DE",
                      "language": "DE",
                      "title": null,
                      "text": "Nein",
                      "description": ""
                    },
                    {
                      "id": "%s-%s-2-EN",
                      "language": "EN",
                      "title": "",
                      "text": "Englisch",
                      "description": ""
                    }
                  ]
                }
              ]
            }
          ],
          "nextLogic": {
            "id": "%s",
            "type": "NEXT_OPTION",
            "count": null,
            "nextQuestionId": null,
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
              {
                "id": "%s-opt1",
                "order": null,
                "type": "NEXT",
                "number": null,
                "count": null,
                "secondNumber": null,
                "secondCount": null,
                "questionAnswerOptionId": "%s-%s-1",
                "secondQuestionAnswerOptionId": null,
                "questionId": "XY",
                "refQuestionId": null
              },
              {
                "id": "%s-opt2",
                "order": null,
                "type": "NEXT",
                "number": null,
                "count": null,
                "secondNumber": null,
                "secondCount": null,
                "questionAnswerOptionId": "%s-%s-2",
                "secondQuestionAnswerOptionId": null,
                "questionId": "XY",
                "refQuestionId": null
              }
            ],
            "refAdaptions": []
          }
        },'''% (id_base, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base, texts[0], id_base, create_content_block(id_base,2, contents, texts),id_base, get_content_length(contents), get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), id_base, id_base, id_base, get_content_length(contents),  id_base, id_base, get_content_length(contents)),
        "OPEN_QUESTION": '''
        {
          "id": "%s",
          "type": "OPEN_QUESTION",
          "number": null,
          "minNumber": null,
          "maxNumber": null,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [
            {
              "id": "%s-DE",
              "language": "DE",
              "title": "",
              "text": "",
              "notAnsweredText": null
            },
            {
              "id": "%s-EN",
              "language": "EN",
              "title": "",
              "text": "",
              "notAnsweredText": null
            }
          ],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": "",
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s     
            ,{
              "id": "%s-%s",
              "type": "ANSWER_OPTION",
              "required": true,
              "showHidden": null,
              "order": %s,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [],
              "answerOptions": [
                {
                  "id": "%s-%s-1",
                  "order": 1,
                  "number": null,
                  "type": "TEXT_FIELD",
                  "imageName": null,
                  "hidden": null,
                  "escapeOption": null,
                  "sliderType": null,
                  "negative": null,
                  "unselectOthers": null,
                  "booleanHelper": null,
                  "refQuestionAnswerOptionId": null,
                  "secondRefQuestionAnswerOptionId": null,
                  "questionLoopCycleId": null,
                  "translations": []
                }
              ]
            }
          ],
          "nextLogic": {
            "id": "%s",
            "type": "%s",
            "count": null,
            "nextQuestionId": "%s",
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
            %s
            ],
            "refAdaptions": []
          }
        },''' % (id_base, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base, id_base,id_base,texts[0], id_base,create_content_block(id_base, 2, contents, texts), id_base, get_content_length(contents), get_content_length(contents), id_base, get_content_length(contents), id_base, next_logic_type,id_base_next_question,create_nextLogic_options(id_base, get_content_length(contents), next_logics, next_logic_type)),
        "SCALA_SLIDER":'''
        {
          "id": "%s",
          "type": "SCALA_SLIDER",
          "number": null,
          "minNumber": %s,
          "maxNumber": %s,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": null,
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s
            ,{
              "id": "%s-%s",
              "type": "ANSWER_OPTION",
              "required": true,
              "showHidden": null,
              "order": %s,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [],
              "answerOptions": [
                {
                  "id": "%s-%s-1",
                  "order": 1,
                  "number": null,
                  "type": "SLIDER",
                  "imageName": null,
                  "hidden": null,
                  "escapeOption": null,
                  "sliderType": null,
                  "negative": null,
                  "unselectOthers": null,
                  "booleanHelper": null,
                  "refQuestionAnswerOptionId": null,
                  "secondRefQuestionAnswerOptionId": null,
                  "questionLoopCycleId": null,
                  "translations": [
                    {
                      "id": "%s-%s-1-DE",
                      "language": "DE",
                      "title": null,
                      "text": "%s, ,%s",
                      "description": ""
                    },
                    {
                      "id": "%s-%s-1-EN",
                      "language": "EN",
                      "title": null,
                      "text": "Englisch",
                      "description": ""
                    }
                  ]
                }
              ]
            }
          ],
          "nextLogic": {
            "id": "%s",
            "type": "%s",
            "count": null,
            "nextQuestionId": "%s",
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
            %s
            ],
            "refAdaptions": []
          }
        },''' % (id_base,question.scala_min,question.scala_max, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base,texts[0], id_base, create_content_block(id_base, 2, contents, texts) ,id_base, get_content_length(contents), get_content_length(contents), id_base, get_content_length(contents), id_base, get_content_length(contents), question.scala_min_text, question.scala_max_text,id_base, get_content_length(contents), id_base, next_logic_type,id_base_next_question,create_nextLogic_options(id_base, get_content_length(contents), next_logics, next_logic_type)),
        "ITEM_LIST_EXPANDABLE": '''
        {
          "id": "%s",
          "type": "ITEM_LIST_EXPANDABLE",
          "number": null,
          "minNumber": 1,
          "maxNumber": %s,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [
            {
              "id": "%s-DE",
              "language": "DE",
              "title": "",
              "text": "",
              "notAnsweredText": null
            },
            {
              "id": "%s-EN",
              "language": "EN",
              "title": "",
              "text": "",
              "notAnsweredText": null
            }
          ],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": "",
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s
            ,{
              "id": "%s-%s",
              "type": "ANSWER_OPTION",
              "required": %s,
              "showHidden": null,
              "order": %s,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [],
              "answerOptions": [
                %s
              ]
            }
          ],
          "nextLogic": {
            "id": "%s",
            "type": "%s",
            "count": null,
            "nextQuestionId": "%s",
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
              %s
            ],
            "refAdaptions": []
          }
        },''' % (id_base, question.maxNumber, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base, id_base,id_base, texts[0], id_base,create_content_block(id_base, 2, contents, texts), id_base, get_content_length(contents), question.answer_required, get_content_length(contents), create_answer_options(question, id_base, get_content_length(contents),answer_options, texts), id_base, next_logic_type, id_base_next_question, create_nextLogic_options(id_base, get_content_length(contents), next_logics, next_logic_type)),
        "ITEM_LIST_SINGLE_CHOICE": '''
        {
          "id": "%s",
          "type": "ITEM_LIST_SINGLE_CHOICE",
          "number": null,
          "minNumber": null,
          "maxNumber": null,
          "screenDuration": null,
          "reviewAble": null,
          "noAnswerPreselection": null,
          "showHint": null,
          "progress": %s,
          "worldObjectEntryKeyType": null,
          "nonOptionalKeyInsightHint": false,
          "optional": true,
          "firstJourneyQuestion": %s,
          "firstSessionQuestion": %s,
          "questionLoopId": null,
          "translations": [
            {
                "id": "%s-DE",
                "language": "DE",
                "title": null,
                "text": "XY"
            },
            {
                "id": "%s-EN",
                "language": "EN",
                "title": null,
                "text": "Englisch"
            }
          ],
          "content": [
            {
              "id": "%s-1",
              "type": "SUB_TITLE",
              "required": null,
              "showHidden": null,
              "order": 1,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "downloadName": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "contentShowType": null,
              "worldObjectEntryKey": null,
              "refQuestionId": null,
              "refQuestionAnswerOptionId": null,
              "translations": [
                {
                  "id": "%s-1-DE",
                  "language": "DE",
                  "title": null,
                  "text": "%s"
                },
                {
                  "id": "%s-1-EN",
                  "language": "EN",
                  "title": null,
                  "text": "Englisch"
                }
              ],
              "answerOptions": []
            }%s
            ,{
              "id": "%s-%s",
              "type": "ANSWER_OPTION",
              "required": true,
              "showHidden": null,
              "order": %s,
              "imageName": null,
              "audioName": null,
              "style": null,
              "refAdaptionType": null,
              "refAdaptionNumber": null,
              "refOrderType": null,
              "refOrderColumn": null,
              "refOffset": null,
              "refLimit": null,
              "checkForSpecialTextReplacement": null,
              "questionAnswerOptionId": null,
              "language": null,
              "refQuestionId": null,
              "translations": [],
              "answerOptions": [
                %s
              ]
            }
          ],
          "nextLogic": {
            "id": "%s",
            "type": "%s",
            "count": null,
            "nextQuestionId": "%s",
            "prevQuestionId": null,
            "refQuestionId": null,
            "questionRefLogicId": null,
            "sessionId": null,
            "options": [
              %s
            ],
            "refAdaptions": []
          }
        },'''%(id_base, question.progress, "true" if count == 0 and write_beginning == True else "null", "true" if count == 0 and write_beginning == True else "null", id_base, id_base, id_base, id_base,texts[0], id_base, create_content_block(id_base,2,contents, texts), id_base, get_content_length(contents), get_content_length(contents), create_answer_options(question, id_base, get_content_length(contents),answer_options, texts), id_base, next_logic_type,id_base_next_question, create_nextLogic_options(id_base, get_content_length(contents), next_logics, next_logic_type))
        }.get(type, None) 
    #return questions_dict[type]