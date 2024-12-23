# Create a playlist.m3u8 file
with open("playlist.m3u8", "w") as file:
    # Write the headers
    file.write("#EXTM3U\n")
    file.write("#EXT-X-VERSION:3\n")
    file.write("#EXT-X-TARGETDURATION:10\n")
    file.write("#EXT-X-MEDIA-SEQUENCE:0\n")
    
    # Write the media segment details
    file.write("#EXTINF:10.0,\n")
    file.write("segment0.ts\n")
    file.write("#EXTINF:10.0,\n")
    file.write("segment1.ts\n")
    file.write("#EXTINF:10.0,\n")
    file.write("segment2.ts\n")
    
    # End of the playlist
    file.write("#EXT-X-ENDLIST\n")

print("playlist.m3u8 file created successfully!")
