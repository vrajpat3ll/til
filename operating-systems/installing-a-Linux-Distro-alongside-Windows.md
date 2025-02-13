# Installing a Linux Distro alongside Windows

- My machine: Dell XPS 15 9520 with Windows 11 Home

- Linux Distro: I guess it is Ubuntu-based (`Pop!_OS`)

## Pre-requisites

- Disable and then re-enable the following things after completely doing the dual boot procedure:

  - paging
  - hibernate
  - system secure
  - secure boot

- Paging

  - Go to `View advanced system settings` > Performance > Settings > Advanced > Virtual Memory > Change.
  - Uncheck `Automatically manage paging file size for all drives`.
  - Select `No paging file`.
  - Apply the changes and restart your computer.
  - To undo this, go to afore-mentioned location and check the box, then aplly changes and restart.

- Hibernate

  - Open command prompt as Administrator.
  - Enter this command in it.
    ```shell
    powercfg.exe /h off
    ```
  - Exit the terminal.
  - To undo this, enter this command in cmd as Admin:
    ```
    powercfg.exe /h on
    ```

- System Secure

  - Go to `View advanced system settings` > System Protection.
  - Select the drive which you want to partition.
  - Press `Configure` > Disable system protection > Delete > OK.
  - To undo this, Go to `View advanced system settings` > System Protection.
  - Select that drive.
  - Press `Configure` > Turn on system protection.

## Steps

| Sr No | Description                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Download an image file (ISO format) of the specific OS according to your device                                                                 |
| 2     | Get an empty USB, we'll make it a bootable USB so it's gonna be formatted                                                                       |
| 3     | Partition some 50-200 GB of space in your drive for Linux                                                                                       |
| 4     | Using Rufus or Balena Etcher, flash the ISO image file of the OS to USB                                                                         |
| 5     | Restart your computer                                                                                                                           |
| 6     | While it is restarting, open Boot configuration menu using (F2 on my machine) F2, F9, F12 or ESC key                                            |
| 7     | Change the order of BOOT menu so that the USB is at the top                                                                                     |
| 8     | (Disable secure boot if ISO is not from an authorised source)                                                                                   |
| 9     | Apply changes and exit                                                                                                                          |
| 10    | Now, you'll be entering your OS                                                                                                                 |
| 11    | Once in OS, you'll be asked to install OS (or similar) -> click on modify partitions                                                            |
| 12    | We'll need the unallocated empty partition here to install linux, store its boot option, and/or swap portion                                    |
| 13    | In Gparted, assign 1 GB to boot section, 4-8 GB of swap storage (linux-swap filesystem), and the remaining to root (ext4 or btrfs)              |
| 14    | After partitioning, assign each of the new partitions to it respective thing (boot, swap, root) and then restart                                |
| 15    | After that, open `disks`, and play the partition where Windows BOOT loader is, mounting it to your system and open it through the link provided |
| 16    | Now from file manager, open your boot manager from /boot/efi                                                                                    |
| 17    | Copy the EFI/Windows directory inside /boot/efi/                                                                                                |
| 18    | Edit the /boot/loader/loader.conf to file and append `timeout 10` to it so that we get 10 seconds to change the boot manager/OS at startup      |
| 19    | Now, all set!                                                                                                                                   |

## ISSUE

- Windows asks about recovery key after startup. How to fix?
  - _Simple_. Just _turn on_ `secure boot` in BIOS options>Boot configuration.

<h5 style="text-align: right;">
    <em>last updated on 13th February, 2025</em>
<h6>
