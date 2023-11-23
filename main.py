import yaml
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import pandas
import matplotlib
matplotlib.use('TkAgg')


with open('legend.yaml') as fh:
    legend = yaml.safe_load(fh)

class PlotMap:
    @classmethod
    def plot(cls, maps):
        length = len(maps)
        fig, axs = plt.subplots(length, 4, sharey=True)
        if length == 1:
            axs = axs.reshape(1,2)

        for en, mapp in enumerate(maps):
            axs[en,0].imshow(mapp.layerBackGround())
            axs[en,0].set_title('BackGround ({})'.format(mapp.name))

            axs[en,1].imshow(mapp.layerForeGround())
            axs[en,1].set_title('ForeGround ({})'.format(mapp.name))

            axs[en,2].imshow(mapp.layerClssIntere())
            axs[en,2].set_title('ClassIntere ({})'.format(mapp.name))

            axs[en,3].imshow(mapp.layerAll())
            axs[en,3].set_title('All ({})'.format(mapp.name))
 



class Map:
    def __init__(self, name, filePath, classInterestId):
        self.name = name
        with rasterio.open(filePath) as image:
            mat = image.read()


        self.mat = mat


        self.backGroundId = 1
        self.backGround = (self.mat == 0)*1

        self.foreGroundId = 2
        self.foreGround = (self.backGround == 0)*1

        self.clssIntereId = classInterestId
        self.clssIntere = (mat == classInterestId)*1


    def layerBackGround(self):
        return self.backGround[0,:,:]


    def layerForeGround(self):
        return self.foreGround[0,:,:]


    def layerClssIntere(self):
        return self.clssIntere[0,:,:]


    def layerAll(self):
        return ( self.foreGroundId*(1 - self.clssIntere)*self.foreGround \
                + self.clssIntereId*self.clssIntere )[0,:,:]




if __name__ == '__main__':
    cam2022 = Map(
          name = 'Campinas2022'
        , filePath = './MAPBIOMAS-EXPORT/mapbiomas-brazil-collection-80-campinas-2022.tif'
        , classInterestId = 3
    )


    cam2021 = Map(
          name = 'Campinas2021'
        , filePath = './MAPBIOMAS-EXPORT/mapbiomas-brazil-collection-80-campinas-2021.tif'
        , classInterestId = 3
    )





    PlotMap.plot([cam2022, cam2021])
    plt.show()

