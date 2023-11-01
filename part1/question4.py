import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. They use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
    SELECT A.name, A.species, A.age 
    FROM animals A 
    LEFT JOIN people_animals PA ON A.animal_id = PA.pet_id 
    WHERE PA.pet_id IS NULL;
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
    SELECT COUNT(DISTINCT(A.animal_id)) 
    FROM animals A 
    JOIN people_animals PA ON A.animal_id = PA.pet_id
    JOIN people P ON PA.owner_id = P.person_id
    WHERE A.age > P.age;
"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 
    SELECT P.name, A.name, A.species
    FROM animals A, people_animals PA, people P
    WHERE A.animal_id = PA.pet_id 
      AND PA.owner_id = P.person_id
      AND P.person_id = 2
      AND A.animal_id NOT IN (
        SELECT A.animal_id 
        FROM animals A, people_animals PA
        WHERE A.animal_id = PA.pet_id
          AND PA.owner_id != 2
      );
"""