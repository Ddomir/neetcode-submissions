class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, j = 0, len(people) - 1
        bCount = 0
        people.sort()

        while i < j:
            print(str(i) + " = " + str(people[i]))
            print(str(j) + " = " + str(people[j]))
            
            if people[j] + people[i] > limit: # Lightest + Heaviest over limit
                bCount += 1
                if people[i] > people[j]:
                    i += 1
                else:
                    j -= 1 # Only heaviest goes
                
                if i == j: # Last person
                    bCount += 1
            
            else:
                bCount += 1 # Heaviest + Lightest
                i += 1
                j -= 1

                if i == j: # Last person
                    bCount += 1
        
            print()

        return bCount
        