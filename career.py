# Challenge 

career_options = ['Medicine', 'Computer Science']

medicine_career_advice = ['1.Medical careers are always in demand', '2.It is a lucrative career path']
CS_career_advice = ['1.Pursue knowledge outside the course', '2.Avoid last minute studying ']
career_questions = ['1.Do you like computers and Mathematics(yes/no)?','2.Are you a caring person and would like to spend much time in hospital(yes/no)?']

print('Answer the following questions to help us determine your career')
print()
print(career_questions[0])
answer_1 = input()
print()
print(career_questions[1])
answer_2 = input()
print()
print('Below is our suggestion for you')
print()

if answer_1 == 'yes' and answer_2 == 'no':
    print('Consider taking a career in {}'.format(career_options[1]))
    print('And this is our advice for you:')
    print(CS_career_advice[0])
    print(CS_career_advice[1])

elif answer_1 == 'no' and answer_2 == 'yes':
    print('Consider taking a career in {}'.format(career_options[0]))
    print('And this is our advice for you:')
    print(medicine_career_advice[0])
    print(medicine_career_advice[1])



elif answer_1 == 'no' and answer_2 == 'no':
    print('Sorry! It seems that your preference do not match the careers available')

else: 
    print('Oops! You entered a wrong input, use small letters only')