# first we will take input of what nominee what we want to keep
nominee1 = input("enter the name of 1st nominee: ")
nominee2 = input("enter the name of 2nd nominee: ")

#  initially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

no_of_voter = len(voter_id)
while True:
    if voter_id == []:  # to check when voter list is completed
        print("voting session is over !!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1, "has won the election with ", percent, "% of votes")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2, "has won the election with ", percent, "% of votes")
            break
        else:
            print("both got equal votes !! government will decide")
            break

    voter = int(input("enter your voter id: "))
    if voter in voter_id:
        print("you are a voter ")
        voter_id.remove(voter)
        print("-------------------------------")
        print("to give vote to ", nominee1, "press 1")
        print("to give vote to ", nominee2, "press 2")
        print("-------------------------------")
        vote = int(input("enter your precious vote: "))
        if vote == 1:
            nm1_votes += 1
            print(nominee1, "thanks you to give your import vote to them !!")
        elif vote == 2:
            nm2_votes += 1
            print(nominee1, "thanks you to give your import vote to them !!")
        elif vote > 2:
            print("check your pressed key !!")
        else:
            print("you are not a voter ")
