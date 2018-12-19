import torch
from torch import nn

class SimpleCNN2Layer(nn.Module):
    def __init__(self):
        super(SimpleCNN2Layer, self).__init__()

        self.conv1 = nn.Conv1d(
            in_channels = 1,
            out_channels = 5,
            kernel_size = 25,
            stride = 1,
            padding = 12
        )

        self.conv2 = nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 1,
            kernel_size = 15,
            stride = 1,
            padding = 7
        )

        self.fc1 = nn.Linear(
            in_features = 4000*self.conv2.out_channels,
            out_features = 4000
        )

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)

        x = leaky(self.conv1(x))
        x = leaky(self.conv2(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = torch.sigmoid(self.fc1(x))

        return x


class SimpleCNN3Layer(nn.Module):
    def __init__(self):
        super(SimpleCNN3Layer, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 10,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 5,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv3.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)

        x = leaky(self.conv1(x))
        x = leaky(self.conv2(x))
        x = leaky(self.conv3(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv3dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x
class SimpleCNN3Layer_A(nn.Module):
    def __init__(self):
        super(SimpleCNN3Layer_A, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 5,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv3.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = leaky(self.conv3(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv3dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x

class SimpleCNN4Layer_A(nn.Module):
    def __init__(self):
        super(SimpleCNN4Layer_A, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 25,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 10,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."

        self.conv4=nn.Conv1d(
            in_channels = self.conv3.out_channels,
            out_channels = 1,
            kernel_size = 3,
            stride = 1,
            padding = (3 - 1) // 2
        )

        assert self.conv4.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv4.out_channels,
            out_features = 4000)


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.35)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        ## print('x.shape after conv1 = ',x.shape)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        ## print('x.shape after conv2 = ', x.shape)
        x = leaky(self.conv3(x))
        ## print('x.shape after conv3 = ', x.shape)
      
        x = self.conv4(x)
        ## print('x.shape after conv4 = ',x.shape)

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x


class SimpleCNN3Layer_B(nn.Module):
    def __init__(self):
        super(SimpleCNN3Layer_B, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv3.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        x = leaky(self.conv3(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv3dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x

class SimpleCNN3Layer_C(nn.Module):
    def __init__(self):
        super(SimpleCNN3Layer_C, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv3.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        x = leaky(self.conv3(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv3dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x
class All_CNN3Layer_C(nn.Module):
    def __init__(self):
        super(All_CNN3Layer_C, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv3.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        ## x = leaky(self.conv3(x))
        ## 180825 try removing the fully connected layer and simply
        ## use the output of the third CVN layer as  input to
        ## the sigmoid function producing the predicted values
        x = self.conv3(x)

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        ## mds x = self.conv3dropout(x)
        ## mds x = self.fc1(x)

        x = torch.sigmoid(x)

        return x
class SimpleCNN4Layer_C(nn.Module):
    def __init__(self):
        super(SimpleCNN4Layer_C, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."

        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv4=nn.Conv1d(
            in_channels = self.conv3.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv4.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.15)
        self.conv4dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv4.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        x = leaky(self.conv3(x))
        x = self.conv3dropout(x)
        x = leaky(self.conv4(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv4dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x
class SimpleCNN5Layer_C(nn.Module):
    def __init__(self):
        super(SimpleCNN5Layer_C, self).__init__()

        self.conv1=nn.Conv1d(
            in_channels = 1,
            out_channels = 20,
            kernel_size = 25,
            stride = 1,
            padding = (25 - 1) // 2
        )

        assert self.conv1.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv2=nn.Conv1d(
            in_channels = self.conv1.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv2.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."

        self.conv3=nn.Conv1d(
            in_channels = self.conv2.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv3.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."

        self.conv4=nn.Conv1d(
            in_channels = self.conv3.out_channels,
            out_channels = 10,
            kernel_size = 15,
            stride = 1,
            padding = (15 - 1) // 2
        )

        assert self.conv4.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv5=nn.Conv1d(
            in_channels = self.conv4.out_channels,
            out_channels = 1,
            kernel_size = 5,
            stride = 1,
            padding = (5 - 1) // 2
        )

        assert self.conv5.kernel_size[0] % 2 == 1, "Kernel size should be odd for 'same' conv."


        self.conv1dropout = nn.Dropout(0.15)
        self.conv2dropout = nn.Dropout(0.15)
        self.conv3dropout = nn.Dropout(0.15)
        self.conv4dropout = nn.Dropout(0.15)
        self.conv5dropout = nn.Dropout(0.35)

        self.fc1 = nn.Linear(
            in_features = 4000 * self.conv5.out_channels,
            out_features = 4000)

    def forward(self, x):
        leaky = nn.LeakyReLU(0.01)
        x = leaky(self.conv1(x))
        x = self.conv1dropout(x)
        x = leaky(self.conv2(x))
        x = self.conv2dropout(x)
        x = leaky(self.conv3(x))
        x = self.conv3dropout(x)
        x = leaky(self.conv4(x))
        x = self.conv4dropout(x)
        x = leaky(self.conv5(x))

        # Remove empty middle shape diminsion
        x = x.view(x.shape[0], x.shape[-1])

        x = self.conv5dropout(x)
        x = self.fc1(x)

        x = torch.sigmoid(x)

        return x