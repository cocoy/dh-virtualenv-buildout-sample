from twisted.application.service import ServiceMaker
 
Sample = ServiceMaker(
    "Sample",
    "sample.tap",
    "Twisted sample application",
    "sample"
)

