import usb, usb.backend.libusb1
backend = usb.backend.libusb1.get_backend(find_library=lambda x: '.\\libusb-1.0.24\\MinGW64\\dll\\libusb-1.0.dll')
dev = usb.core.find(backend=backend, find_all=True)
for cfg in dev:
    print('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct))
    print('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')