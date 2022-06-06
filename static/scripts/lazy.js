const overhead = window.innerHeight / 2
const bottom_visible = element => element.getClientRects()[0].bottom < window.innerHeight + overhead
