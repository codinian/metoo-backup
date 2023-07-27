import os
import sys
import argparse
import facebook_scraper as fs

def get_post_content(url, cookies):
  if cookies != None:
    gen = fs.get_posts(post_urls=[url], cookies=cookies)
  else:
    gen = fs.get_posts(post_urls=[url])
  post = next(gen)
  time_str = post['time'].strftime('%Y-%m-%d')
  return post['username'], time_str, post['text']

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--url', required=True, type=str, help='The URL of Facebook post')
  parser.add_argument('--filename', required=True, type=str, help='Output filename')
  parser.add_argument('--cookies', type=str, help='Path of cookies.json')
  args = parser.parse_args()

  author, time_dir, content = get_post_content(args.url, args.cookies)

  if not os.path.exists(time_dir):
    os.makedirs(time_dir)

  if args.filename.endswith(".md"):
    filename = args.filename
  else:
    filename = args.filename + ".md"

  file_path = os.path.join(time_dir, filename)
  with open(file_path, "w") as file:
    file.write(f"# {filename.split('.')[0]}\n")
    file.write(f"Author: {author}\n")
    file.write(content)

if __name__ == '__main__':
  main()
