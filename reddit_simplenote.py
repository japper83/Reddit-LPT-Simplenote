import praw
import yaml
import simplenote

number_of_upvotes = 10000
time_filter = 'week'  # you can use all, day, hour, month, week,
# year (default: all).
limit_posts = 20

sn = simplenote.Simplenote("simplenote e-mail", "simplenote password")
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')


def read_config():
    with open('config.yaml', 'r') as f:
        config = yaml.load(f)
    return config


def write_config(data_to_write):
    with file("config.yaml", 'w') as f:
        yaml.dump(data_to_write, f)


config = read_config()
for submission in reddit.subreddit('lifeprotips').top(time_filter=time_filter,
                                                      limit=limit_posts):
    if submission.id not in config and submission.score >= number_of_upvotes:
        config.append(submission.id)
        write_config(config)
        text = {'content': submission.title + '\n\n\n' + submission.selftext + '\n\n\n' + submission.url}
        sn.add_note(text)
        print submission.url
