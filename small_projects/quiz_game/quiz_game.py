"""
Quiz Game
Author: Satria Dwi Cahya
Purpose: To understand storage questions using a dictionary and a list.
"""
# Module Import Section
import os
import random

# digunakan untuk keyword dicitonary nantinya
QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'
VALID_OPTIONS = ['A', 'B', 'C', 'D'] 

# Untuk membersihkan teks pada terminal
def clear_screen():
    os.system('cls')

# Menyambut pengguna agar terasa lebih dekat
def welcome_sign():
    print('Quiz Game')
    print('---------')


# -----
# Gamee
# -----


# Memberikan pertanyaan ke user
def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)   
    
    control_variable = True
    while control_variable:
        user_answer = input('Your answer: ').upper().strip()
        
        if user_answer not in VALID_OPTIONS:
            print('Please input right option!')
        else:
            control_variable = False
            return user_answer 




# Mengacak pertanyaan, menentukan jawaban benar, dan menentukan skor
def run_quiz(quiz):
    clear_screen()
    welcome_sign()
    random.shuffle(quiz)

    score = 0
    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            print('Correct!')
            score +=1
        else:
            print(f'Wrong! The correct answer is {item[ANSWER]}')

        print()
    
    print(f'Your final answer is {score} out of {len(quiz)}')


# Menyimpan pertanyaan dengan list dan dictionary di dalam list
def storage_question():
    quiz = [
        {
            QUESTION : 'Apa yang dimaksud dengan monophthong?',
            OPTIONS : ['A. Dua bunyi vokal yang diucapkan terpisah', 'B. Satu bunyi vokal yang stabil tanpa perubahan', 'C. Bunyi vokal yang selalu panjang','D. Bunyi vokal yang selalu diikuti huruf “e”'],
            ANSWER : 'B',
        },
        {
            QUESTION : 'Kata manakah yang mengandung diphthong?',
            OPTIONS : ['A. cat', 'B. bed','C. time', 'D. Cup'],
            ANSWER : 'C'
        },
        {
            QUESTION : 'Bunyi /aɪ/ pada kata time termasuk jenis apa?',
            OPTIONS : ['A. Short vowel', 'B. Long vowel', 'C. Monophthong', 'D. Diphthong'],
            ANSWER : 'D'
        },
        {
            QUESTION : 'Manakah pasangan kata yang menunjukkan perbedaan monophthong dan diphthong?',
            OPTIONS : ['A. bed–bad', 'B. sit–site', 'C. cup–cap', 'D. hot–hat'],
            ANSWER : 'B'
        },
        {
            QUESTION : 'Pernyataan manakah yang BENAR tentang diphthong?',
            OPTIONS : ['A. Tidak ada gerakan mulut saat mengucapkannya', 'B. Selalu terdiri dari dua suku kata', 'C. Bunyi vokalnya berubah dari satu ke bunyi lain', 'D. Hanya ada pada kata yang panjang'],
            ANSWER : 'C'

        }
    ] 

    run_quiz(quiz)



storage_question()