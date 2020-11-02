import requests
import argparse
import os
import ast

os.environ['NO_PROXY'] = '127.0.0.1'
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query-type', default=None)
    parser.add_argument('--created_on', default=None)
    parser.add_argument('--range_from', default=None)
    parser.add_argument('--range_to', default=None)
    parser.add_argument('--reported_by', default=None)
    parser.add_argument('--assigned_to', default=None)
    # parser.add_argument('--server-port', default="1234")
    parser.add_argument('--entry', default=None)

    server_port = 5000
    with open('server_port.txt','r') as serv:
        server_port = serv.readline()

    args = parser.parse_args()
    base_url = f"http://127.0.0.1:{server_port}"

    def printBugs(result):
        result = ast.literal_eval(result)
        for x in range(len(result)):
            print(result[x])

    if args.query_type == "get_total_number_of_bugs":
        result = requests.get(f"{base_url}/total_number_of_bugs").text
        print(result)
    elif args.query_type == "add_new_bug":
        if args.entry is None:
            raise ValueError("Please provide --entry field.")
        bug_data = {"entry": args.entry}
        result = requests.post(f"{base_url}/add_new_bug", data = bug_data).json()

        message = result["message"]
        print(f"Response is: {message}")
    elif args.query_type == "get_all_bugs_created_on":
        result = requests.get(f"{base_url}/all_bugs_created_on",params={"created_on":args.created_on}).text
        print("Here is a list of all the bugs created on the specified date:")
        printBugs(result)
    elif args.query_type == "get_all_bugs_created_in_range":
        result = requests.get(f"{base_url}/all_bugs_created_in_range", params={"range_from": args.range_from,"range_to": args.range_to}).text
        print("Here is a list of all the bugs created between the specified dates:")
        printBugs(result)
    elif args.query_type == "get_all_bugs_reported_by":
        result = requests.get(f"{base_url}/all_bugs_reported_by", params={"reported_by": args.reported_by}).text
        print("Here is a list of all the bugs reported by:")
        printBugs(result)
    elif args.query_type == "get_all_bugs_assigned_to":
        result = requests.get(f"{base_url}/all_bugs_assigned_to", params={"assigned_to": args.assigned_to}).text
        print("Here is a list of all the bugs assigned to:")
        printBugs(result)