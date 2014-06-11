# Grsecurity Kernels for Enterprise Linux 6
This repo contains the spec files and kernel configurations used to build grsecurity-enabled kernels for EL6. The kernel version tracks the Grsecurity long-term supported kernel -- 3.2.59 as of the time of this writing. The RPM spec file is based off of the kernel spec file used by [ElRepo](http://elrepo.org/).

## Why Grsecurity?
We are big fans of SELinux -- and in fact suggest enabling SELinux along with Grsecurity -- but SELinux only goes so far. Adding Grsecurity provides an extra layer of kernel hardening to help prevent certain attacks that may slip past SELinux. For more information on Grsecurity, see http://grsecurity.net

## Installing Pre-Built Kernels
Pre-built kernel RPMs are provided by Tag1 Consulting, made available at http://pkg.tag1consulting.com/kernel/el6/x86_64/

These can be installed easily with yum by first installing the grsec-kernel-release package which installs the yum repo file and GPG key used to sign the kernel packages.

 1. rpm -Uvh http://pkg.tag1consulting.com/kernel/el6/x86_64/grsec-kernel-release-6-1.noarch.rpm
 2. yum install kernel-ltgrsec

Packages are signed with the GPG key located at http://pkg.tag1consulting.com/RPM-GPG-KEY-TAG1

```
 Key fingerprint = 2B1F 2ACA C636 E756 DD87  4F17 9D03 36F1 C0E9 5DD3
```

## Building Your Own Grsecurity Kernel for Enterprise Linux
The Grsecurity patches use gcc macro expansion that is not supported in the gcc version shipped with EL6. For this to work, we build the kernels using the newer gcc (4.8) packages provided by the [CERN Developer Toolset repo](http://linux.web.cern.ch/linux/devtoolset/). We suggest building the kernel under 'mock', and have provided a mock configuration file which includes the devtoolset-2 repo.

To build a kernel under mock:
 1. Install the 'mock' package, and add your user to the 'mock' group.
 2. Copy mock/el6-devtools2-x86_64.cfg from this repo to /etc/mock on the build system.
 3. Download kernel source and grsec patch specified in the specfile. This can be done automatically with the use of 'spectool', e.g. ```spectool get_sources kernel-ltgrsec-3.2.spec``` and ```spectool get_patches kernel-ltgrsec-3.2.spec```.
 4. Build an SRPM to pass to mock with ```rpmbuild -bs --nodeps kernel-ltgrsec-3.2.spec```.
 5. Build the kernel in a mock chroot with ```mock -r el6-devtools2-x86_64 /path/to/your/kernel.src.rpm```

## Known Issues
The current Grsecurity configuration blocks certain calls used by hald. We have not spent time to troubleshoot this yet, for now we suggest either disabling hald, or if you wait patiently, it should time out during boot and eventually the system will boot up completely.
