screen home_bathroom():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hover ("overlays/bedroom_door1.webp")
            idle ("overlays/bedroom_door0.webp")
            action Call("change_location_to", "Bedroom")
label home_bathroom:
    "this is my home"

    return
    # menu:
    #     "Are you +18 years old?"
    #     "Yes":
    #         "option 1"
    #         call bedroom
    #     "No":
    #         "option 2"
    #         return
