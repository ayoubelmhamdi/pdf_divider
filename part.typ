// #set page(height: 300pt, width: 600pt)

#let pages = 2
#let ll = (
    "aa",
    "bb"
)

#let t(i, txt: "") = {
    align(
        center, [
            #v(1fr)
            #text(size: 60pt, [MISDAQ #v(0.2fr) PART #i])
            #if txt != "" [
                #text(size: 40pt, [#v(0.4fr) #txt])
            ]

            #v(1fr) 
            #if i != pages [
                #pagebreak()
            ]
        ]
    )
}


#for (index, value) in ll.enumerate(){
    t(index+1, txt:value)
}
