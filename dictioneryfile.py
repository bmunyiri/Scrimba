#Dictionaries in Python
# Information about this guy
person = {"name":"joseph","town":"bethlehem","number":20}
print(f"{person["name"]} was born in {person["town"]}\n")

person["town"] ="New York"
print(f" Some of {person["name"]} information has changed, see his town now is {person["town"]}\n")


person["town"] = "London"
print(f" Some of {person["name"]} information has changed, see his town now is {person["town"]}\n")

#Rivers and their countries
rivers ={"nile":"Egypt","amazon":"brazil","congo":"DRC"}

for key,value in rivers.items():
    print(f"\n The river {key} runs in the country of {value}.")


