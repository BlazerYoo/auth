import usb
backend = usb.backend.libusb1.get_backend(find_library=lambda x: '.\\libusb-1.0.24\\MinGW64\\dll\\libusb-1.0.dll')
dev = usb.core.find(backend=backend, find_all=True)
for cfg in dev:
    sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
    sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')