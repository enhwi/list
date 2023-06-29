question_list = ["1.How many continents are there?",
"2.What is the capital of India?", 
"3.What courses are taught in NG?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"], 
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"], 
["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]] 
lifeline_option=[["1.Four","3.Seven"], ["1.Chandigarh","4.Delhi"], 
["1.Software Engineering","2.counseling"]]
question_list1=[3,4,1] 
lifeline_options=[["3.foue","4.nine"],["1.Chennai","4.Delhi"],
["1.Software Engineering","4.Counseling"]]     
i=0
amount=0
c=1
while i<len(question_list):
    print(question_list[i]) 
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j=j+1   
    while c<=1:
        lifeline=input("life line yes or no")
        if lifeline=="yes":
            s=0
            while s<len(lifeline_options[i]):
                print(lifeline_options[i][s])
                s=s+1
        c=c+1      
    select=int(input("Choose any one option")) 
    if select==question_list1[i]:
        amount=amount+1000
        print("your answer is correct you win")
    else:
        print("your answer is wrong") 
        break               
    i=i+1

