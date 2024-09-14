# def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
#     try:
#         reddit = praw.Reddit(client_id=client_id,
#                              client_secret=client_secret,
#                              user_agent=user_agent)
#         print(f"Authenticated as: {reddit.user.me()}")
#         return reddit
#     except prawcore.exceptions.ResponseException as e:
#         print(f"Authentication error: {e}")
#         sys.exit(1)
#
# def extract_post(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
#     try:
#         subreddit = reddit_instance.subreddit(subreddit)
#         posts = subreddit.top(time_filter=time_filter, limit=limit)
#         for post in posts:
#             post_dict = vars(post)
#             print(post_dict)
#     except Exception as e:
#         print(f"Error extracting posts: {e}")
