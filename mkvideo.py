"""Build a hero video out of the client's OWN fleet photographs.

WHY: he has asked three times to get YouTube's interface off his hero. It
cannot be done - the branding and the player controls are not removable, and
the controls sit dead centre over the car so they cannot be cropped away the
way the title bar and wordmark were. The only way to have a video with no
player interface is to not use a video player that draws one. That means a
self-hosted <video> file, and I cannot fetch his chosen clip (YouTube bot-walls
this server, and working around that is not mine to do).

So this makes one from material he already owns: the seven branded all-black
vehicle photographs he sent, including the Escalade with his own LOOK LIMO
plate against the Philadelphia skyline.

LANDSCAPE, not 9:16. The vertical frame only ever existed because the YouTube
clip was a Short. Self-hosting means choosing the shape - and 16:9 both suits
photographs that are all 1.26-1.52 wide and finally lets the video fill the
whole band edge to edge, which he asked for weeks ago and could not have while
it was vertical.

Loops invisibly: it opens from black and closes to black, so the wrap point has
nothing to see.
"""
import os
import subprocess

A = "/var/lib/freelancer/projects/40609577/site/assets"
IMGS = ["hero-image.jpg", "fleet-escalade.jpg", "fleet-aviator.jpg",
        "fleet-suburban.jpg", "fleet-sprinter.jpg", "fleet-minibus.jpg",
        "fleet-bus.jpg"]
# fleet-limobus.jpg is deliberately left out - it is the one stock photo in the
# set (a limo interior), and this video is meant to be entirely his.

HOLD, XF, FPS = 3.4, 0.8, 30
W, H = 1600, 900

ins, filts = [], []
for i, f in enumerate(IMGS):
    ins += ["-loop", "1", "-framerate", str(FPS), "-t", f"{HOLD:.2f}",
            "-i", os.path.join(A, f)]
    # Upscale BEFORE zoompan. Zooming a source at its native size makes the
    # pan judder a pixel at a time; oversampling first hides the steps.
    # Alternate push-in and pull-out so seven clips do not feel mechanical.
    if i % 2 == 0:
        z = f"min(zoom+0.00085,1.14)"
    else:
        z = f"max(1.14-0.00085*on,1.0)"
    filts.append(
        f"[{i}:v]scale=3200:1800:force_original_aspect_ratio=increase,"
        f"crop=3200:1800,setsar=1,"
        f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        f":d=1:s={W}x{H}:fps={FPS},"
        # a light unifying grade - these are already dark and graded, so this
        # only firms up the blacks and warms the highlights toward the gold
        f"eq=contrast=1.06:saturation=1.04,"
        f"colorbalance=rs=0.02:gh=0.01:bs=-0.03[v{i}]")

chain, prev, t = [], "v0", 0.0
for i in range(1, len(IMGS)):
    t += HOLD - XF
    out = f"x{i}"
    chain.append(f"[{prev}][v{i}]xfade=transition=fade:duration={XF}:offset={t:.2f}[{out}]")
    prev = out

total = len(IMGS) * HOLD - (len(IMGS) - 1) * XF
# open from black and close to black so the loop point is invisible
chain.append(f"[{prev}]fade=t=in:st=0:d=0.9,"
             f"fade=t=out:st={total-0.9:.2f}:d=0.9,format=yuv420p[out]")

fc = ";".join(filts + chain)
cmd = (["ffmpeg", "-v", "error", "-stats"] + ins +
       ["-filter_complex", fc, "-map", "[out]",
        "-c:v", "libx264", "-preset", "slow", "-crf", "25",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-an",                      # no audio track at all: it can never
                                    # surprise anyone with sound on load
        "-t", f"{total:.2f}", "hero-fleet.mp4", "-y"])
print(f"{len(IMGS)} photos, {total:.1f}s\n")
subprocess.run(cmd, check=True)
print("\ndone")
