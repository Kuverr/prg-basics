# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   tv1 = TV()


   # object usage
   tv1.turn_on()
   tv1.program_channel('tv2136')
   tv1.show_status()
   tv1.available_channels()
   tv1.set_channel(1)
   tv1.available_channels()
   tv1.show_status()
   tv1.turn_off()

if __name__ == "__main__":
   main() 