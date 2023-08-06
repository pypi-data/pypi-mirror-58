# -*- coding: utf-8 -*-
import pandas as pd
import random

def load_and_type_filter_questions(path= 'questions.csv',type_filter = ['math','letter_input']):
    # df = pd.read_csv(path)
    filter_code = 'filtered_questions = df['
    for i in type_filter:
        filter_code = filter_code + 'df.type.str.contains(\''+i+'\')|'

    filter_code = filter_code[:-1]+']'
    # exec('print(filter_code)')
    temp = {'df':pd.read_csv(path,encoding='utf-8')}
    exec(filter_code, temp)
    filtered_questions = temp['filtered_questions']
    question_index = list(filtered_questions.index)
    return filtered_questions

def load_and_correct_rate_filter_questions(df,correct_fre_filter_threhold,error_fre_filter_threhold,correct_rate_filter_threhold):
    filtered_questions = df[(df['correct fre']<correct_fre_filter_threhold)&(df['error fre']>=error_fre_filter_threhold)&(df['correct rate']<=correct_rate_filter_threhold)]
    return filtered_questions

def generate_question(path= 'questions.csv',type_filter = ['letter_input'],correct_fre_filter_threhold=10000,error_fre_filter_threhold=0,correct_rate_filter_threhold=1):
    filtered_questions1 = load_and_type_filter_questions(path,type_filter=type_filter)
    print(filtered_questions1)
    print('------------------------------------')
    filtered_questions = load_and_correct_rate_filter_questions(filtered_questions1,correct_fre_filter_threhold,error_fre_filter_threhold,correct_rate_filter_threhold)
    print(filtered_questions)
    questions_index = list(filtered_questions.index)
    print(questions_index)
    question_index = random.choice(questions_index)
    return {'question':filtered_questions['question'][question_index],
            'answer':filtered_questions['answer'][question_index],
            'index':question_index}


def count_correct_fre(index,path= 'questions.csv',correct = True):
    df = pd.read_csv(path,encoding='utf-8')
    # print(df['correct fre'][index])
    if correct:
        df.loc[index, 'correct fre'] += 1
        df.loc[index, 'correct rate'] = df.loc[index, 'correct fre']/(df.loc[index, 'correct fre']+df.loc[index, 'error fre'])*100
    else:
        df.loc[index, 'error fre'] += 1
        df.loc[index, 'correct rate'] = df.loc[index, 'correct fre']/(df.loc[index, 'correct fre']+df.loc[index, 'error fre'])*100
    # print(df['correct fre'][index])
    df.to_csv(path,index=False)

def reset_column_to_zero(path= 'questions.csv',column = 'correct fre'):
    df = pd.read_csv(path,encoding='utf-8')
    df.loc[:, column] = 0
    df.to_csv(path,index=False)

def reset_statistics_column():
    reset_column_to_zero(column = 'correct rate')
    reset_column_to_zero(column = 'correct fre')
    reset_column_to_zero(column = 'error fre')

if __name__=='__main__':
    filtered_questions = load_and_type_filter_questions()
    # print(filtered_questions)

    q = generate_question()
    print(q['question'],q['answer'])
    # df = load_and_type_filter_questions(type_filter=['letter input'])

    # print(filtered_questions)
    # count_correct_fre()
    #
    # reset_statistics_column()
    #
    #
    #
    # path= 'questions.csv'
    # df = pd.read_csv(path)
    # filtered_questions = df[(df['correct fre']>0)|(df['correct rate']>1)]
    # print(filtered_questions)




    #
    # df.loc[10, 'correct fre'] += 1
    # print(df['correct fre'][10])
