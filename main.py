import pytube.exceptions
from pytube import YouTube
import sys
from pytube.cli import on_progress

def quit_program(msg) -> NoReturn:
    print(f'Error: {msg}')
    sys.exit(1)


action = ''

try:
    action = sys.argv[1]
    if action == '-d':
        try:
            filetype = sys.argv[2]
            if filetype not in ['mp4', 'webm']:
                quit_program('unsupported filetype')
        except IndexError:
            quit_program('no filetype provided')
        try:
            media = sys.argv[3]
            if media not in ['a', 'v']:
                quit_program('unsupported media')
        except IndexError:
            quit_program('no media provided')
        try:
            link = sys.argv[4]
            yt = YouTube(link, on_progress_callback=on_progress)
            if filetype == 'mp4':
                if media == 'v':
                    stream = yt.streams.get_by_itag(22)
                elif media == 'a':
                    stream = yt.streams.get_by_itag(139)
            elif filetype == 'webm':
                if media == 'v':
                    stream = yt.streams.get_by_itag(248)
                elif media == 'a':
                    stream = yt.streams.get_by_itag(249)
            stream.download('YOUR_PATH')
            print(f"Video saved to 'Downloads' folder as '{yt.title}'.")
        except IndexError:
            quit_program('no video link provided')
        except pytube.exceptions.RegexMatchError:
            quit_program('enter correct YouTube link')
        except AttributeError:
            quit_program('try different filetype or media')
        except:
            quit_program('an unexpected error occurred')
    elif action == '-h':
        print('Welcome to YouTube Downloader')
        print('To download a video of choice use the -d command.')
        print("use -d [filetype] [media] '[link]'")
except IndexError:
    quit_program('no action provided')
