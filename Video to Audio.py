from moviepy.video.io.VideoFileClip import VideoFileClip

# Set the input and output file paths
input_file = 'vvideo.mp4'
output_file = 'vvideoaudio.mp3'

# Open the video file using moviepy
clip = VideoFileClip(input_file)

# Write the audio of the video to an mp3 file
clip.audio.write_audiofile(output_file)
