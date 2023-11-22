import yaml
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import pandas
import matplotlib
matplotlib.use('TkAgg')


with open('legend.yaml') as fh:
    legend = yaml.safe_load(fh)


class Map:
    def __init__(self, name, filePath, classInterestId):
        self.name = name
        with rasterio.open(filePath) as image:
            mat = image.read()


        self.mat = mat

        self.classInterestId = classInterestId

        self.backGround = (self.mat == 0)*1

        self.foreGround = (self.backGround == 0)*1

        self.clssIntere = (mat == classInterestId)*1


    def maskAll(self):
        return self.foreGround + self.clssIntere

    def plot(self):
        fig, axs = plt.subplots(1, 2, sharey=True)

        axs[0].imshow(self.foreGround[0,:,:])
        axs[0].set_title('ForeGround')

        axs[1].imshow(self.clssIntere[0,:,:] + self.foreGround[0,:,:])
        axs[1].set_title('ClassOfInterest {}'.format(self.classInterestId))

        fig.suptitle(self.name)



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




    cam2022.plot()
    cam2021.plot()


    plt.show()

    import IPython; IPython.embed()
