import cairo
import rsvg

img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 640,480)

ctx = cairo.Context(img)

handler= rsvg.Handle("carymap.svg")
# or, for in memory SVG data:
#handler= rsvg.Handle(None, str(<svg data>))

handler.render_cairo(ctx)

img.write_to_png("carymap.png")
