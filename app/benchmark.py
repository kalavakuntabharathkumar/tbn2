import argparse,json
from .tasks import get_tasks
from .agent import demo_agent
from .grader import grade
a=argparse.ArgumentParser();a.add_argument('--episodes',type=int,default=25);args=a.parse_args();ts=get_tasks();rs=[grade((t:=ts[i%len(ts)]),demo_agent(t)).model_dump() for i in range(args.episodes)];print(json.dumps({'episodes':args.episodes,'pass_rate':sum(x['passed'] for x in rs)/len(rs)},indent=2))
