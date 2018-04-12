''' Created on 11 Apr. 2018
Example of using the ris_processing package
@author: James Moran
'''
import ris_processing.read_ris
import ris_processing.file_io_thermal
import ris_processing.process_image

if __name__ == '__main__':
    file = '\n'
    while '.ris' not in file:
        file = input('What file to read? Must be a *.ris file. Default: A35.ris\n')
    f = open(file, 'rb')
    
    print('Reading file...')
    thermogram = ris_processing.read_ris.get_thermogram(f)
    print('Done!')
    
    print('Saving thermogram to .gif...')
    ris_processing.file_io_thermal.save_gif(thermogram, 'thermogram.gif')
    print('Done!')
    
    print('Processing image...')
    phasemap = ris_processing.process_image.process_image(thermogram)
    print('Done!')
    
    print('Saving phasemap to .png...')
    ris_processing.file_io_thermal.save_png(phasemap, 'phase.png')
    f.close()
    print("Done! Process Complete. Press enter to close.")
    input()