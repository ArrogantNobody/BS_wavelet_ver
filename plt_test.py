import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

psnr = 19.456
ep = []
ps = []
for epoch in range(20):
    psnr += 2
    ep.append(epoch+1)
    ps.append(psnr)

plt.plot(ep, ps)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(2))
plt.xlabel('epoch')
plt.ylabel('PSNR')
plt.title("PSNR values during training")
plt.savefig('./net_epoch%d_PSNR%.4f.jpg' % (epoch + 1, psnr))
plt.show()