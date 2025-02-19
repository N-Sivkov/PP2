import json


with open("sample-data.json", "r") as file:
    data = json.load(file)
a = []
for i in data["imdata"]:
    attributes = i["l1PhysIf"]["attributes"]
    a.append({"DN": attributes["dn"], "Description": attributes["descr"], "Speed": attributes["speed"], "MTU": attributes["mtu"]})
print("Interface Status")
print("=" * 89)
print(f"{'DN':<60} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 59 + "  " + "-" * 19 + "   " + "-" * 6 + "   " + "-" * 6)
for i in a:
    print(f"{i['DN']:<60} {i['Description']:<20} {i['Speed']:<10} {i['MTU']:<10}")