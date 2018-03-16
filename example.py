import os
import sys
import time
from api.client import DotmeshClient

# let's set up the cluster access:
api_key = os.environ['DOTMESH_APIKEY']
cluster_url = "http://localhost:6969/rpc"
dmclient = DotmeshClient(cluster_url=cluster_url, username="admin", api_key=api_key)

# now let's create a dot called 'test' and work in a branch called 'master':
dotname = "test"
branchname = "master"
print("== Create dot:")
dot = dmclient.createDot(dotname=dotname)
# alternatively, if a dot already exists,
# you can do the following:
# dot = dmclient.getDot(dotname=dotname)
print("\nID={0}, name={1}".format(dot.id, dot.name))

# get a branch to work on:
print("\n== Get master branch:")
branch = dot.getBranch(branchname)
print("\n{0}".format(branch.name))

# now let's do a commit:
print("\n== Do some commit and show log:")
branch.commit("just a test commit")
branch.commit("and another commit, who would have thought")
log = branch.log()
print("\n")
for entry in log:
    msg = entry["Metadata"]["message"]
    ctime = entry["Metadata"]["timestamp"]
    print("{0}: {1}".format(ctime, msg))

# time for a new branch:
print("\n== Create new branch, commit and show log:")
mybranch = branch.createBranch("mybranch", "master")
mybranch.commit("the first commit in my branch")
mylog = mybranch.log()
print("\n")
print("{0}: {1}".format(mylog[0]["Metadata"]["timestamp"], mylog[0]["Metadata"]["message"]))

# and finally, let's clean up by deleting the dot (and all the commits)
print("\n== Clean-up:")
if len(sys.argv) > 1 and sys.argv[1]=="cleanup":
    dmclient.deleteDot(dotname=dotname)
