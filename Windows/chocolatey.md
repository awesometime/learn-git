### 1 chocolatey安装    管理员身份
```shell
C:\Windows\system32>@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
Getting latest version of the Chocolatey package for download.
Getting Chocolatey from https://chocolatey.org/api/v2/package/chocolatey/0.10.11.
Downloading 7-Zip commandline tool prior to extraction.
Extracting C:\Users\lx\AppData\Local\Temp\chocolatey\chocInstall\chocolatey.zip to C:\Users\lx\AppData\Local\Temp\chocolatey\chocInstall...
Installing chocolatey on this machine
Creating ChocolateyInstall as an environment variable (targeting 'Machine')
  Setting ChocolateyInstall to 'C:\ProgramData\chocolatey'
WARNING: It's very likely you will need to close and reopen your shell
  before you can use choco.
Restricting write permissions to Administrators
We are setting up the Chocolatey package repository.
The packages themselves go to 'C:\ProgramData\chocolatey\lib'
  (i.e. C:\ProgramData\chocolatey\lib\yourPackageName).
A shim file for the command line goes to 'C:\ProgramData\chocolatey\bin'
  and points to an executable in 'C:\ProgramData\chocolatey\lib\yourPackageName'.

Creating Chocolatey folders if they do not already exist.

WARNING: You can safely ignore errors related to missing log files when
  upgrading from a version of Chocolatey less than 0.9.9.
  'Batch file could not be found' is also safe to ignore.
  'The system cannot find the file specified' - also safe.
chocolatey.nupkg file not installed in lib.
 Attempting to locate it from bootstrapper.
PATH environment variable does not have C:\ProgramData\chocolatey\bin in it. Adding...
警告: Not setting tab completion: Profile file does not exist at
'C:\Users\lx\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'.
Chocolatey (choco.exe) is now ready.
You can call choco from anywhere, command line or powershell by typing choco.
Run choco /? for a list of functions.
You may need to shut down and restart powershell and/or consoles
 first prior to using choco.
Ensuring chocolatey commands are on the path
Ensuring chocolatey.nupkg is in the lib folder

C:\Windows\system32>choco
Chocolatey v0.10.11
Please run 'choco -?' or 'choco <command> -?' for help menu.

C:\Windows\system32>choco -?
This is a listing of all of the different things you can pass to choco.

Commands

 * list - lists remote or local packages
 * search - searches remote or local packages (alias for list)
 * info - retrieves package information. Shorthand for choco search pkgname --exact --verbose
 * install - installs packages from various sources
 * pin - suppress upgrades for a package
 * outdated - retrieves packages that are outdated. Similar to upgrade all --noop
 * upgrade - upgrades packages from various sources
 * uninstall - uninstalls a package
 * pack - packages up a nuspec to a compiled nupkg
 * push - pushes a compiled nupkg
 * new - generates files necessary for a chocolatey package from a template
 * sources - view and configure default sources (alias for source)
 * source - view and configure default sources
 * config - Retrieve and configure config file settings
 * features - view and configure choco features (alias for feature)
 * feature - view and configure choco features
 * setapikey - retrieves or saves an apikey for a particular source (alias for apikey)
 * apikey - retrieves or saves an apikey for a particular source
 * unpackself - have chocolatey set itself up
 * version - [DEPRECATED] will be removed in v1 - use `choco outdated` or `cup <pkg|all> -whatif` instead
 * update - [DEPRECATED] RESERVED for future use (you are looking for upgrade, these are not the droids you are looking for)


Please run chocolatey with `choco command -help` for specific help on
 each command.

How To Pass Options / Switches

You can pass options and switches in the following ways:

 * Unless stated otherwise, an option/switch should only be passed one
   time. Otherwise you may find weird/non-supported behavior.
 * `-`, `/`, or `--` (one character switches should not use `--`)
 * **Option Bundling / Bundled Options**: One character switches can be
   bundled. e.g. `-d` (debug), `-f` (force), `-v` (verbose), and `-y`
   (confirm yes) can be bundled as `-dfvy`.
 * NOTE: If `debug` or `verbose` are bundled with local options
   (not the global ones above), some logging may not show up until after
   the local options are parsed.
 * **Use Equals**: You can also include or not include an equals sign
   `=` between options and values.
 * **Quote Values**: When you need to quote an entire argument, such as
   when using spaces, please use a combination of double quotes and
   apostrophes (`"'value'"`). In cmd.exe you can just use double quotes
   (`"value"`) but in powershell.exe you should use backticks
   (`` `"value`" ``) or apostrophes (`'value'`). Using the combination
   allows for both shells to work without issue, except for when the next
   section applies.
 * **Periods in PowerShell**: If you need to pass a period as part of a
   value or a path, PowerShell doesn't always handle it well. Please
   quote those values using "Quote Values" section above.
 * **Pass quotes in arguments**: When you need to pass quoted values to
   to something like a native installer, you are in for a world of fun. In
   cmd.exe you must pass it like this: `-ia "/yo=""Spaces spaces"""`. In
   PowerShell.exe, you must pass it like this: `-ia '/yo=""Spaces spaces""'`.
   No other combination will work. In PowerShell.exe if you are on version
   v3+, you can try `--%` before `-ia` to just pass the args through as is,
   which means it should not require any special workarounds.
 * Options and switches apply to all items passed, so if you are
   installing multiple packages, and you use `--version=1.0.0`, choco
   is going to look for and try to install version 1.0.0 of every
   package passed. So please split out multiple package calls when
   wanting to pass specific options.

Default Options and Switches

 -?, --help, -h
     Prints out the help menu.

 -d, --debug
     Debug - Show debug messaging.

 -v, --verbose
     Verbose - Show verbose messaging. Very verbose messaging, avoid using
       under normal circumstances.

     --trace
     Trace - Show trace messaging. Very, very verbose trace messaging. Avoid
       except when needing super low-level .NET Framework debugging. Available
       in 0.10.4+.

     --nocolor, --no-color
     No Color - Do not show colorization in logging output. This overrides
       the feature 'logWithoutColor', set to 'False'. Available in 0.10.9+.

     --acceptlicense, --accept-license
     AcceptLicense - Accept license dialogs automatically. Reserved for
       future use.

 -y, --yes, --confirm
     Confirm all prompts - Chooses affirmative answer instead of prompting.
       Implies --accept-license

 -f, --force
     Force - force the behavior. Do not use force during normal operation -
       it subverts some of the smart behavior for commands.

     --noop, --whatif, --what-if
     NoOp / WhatIf - Don't actually do anything.

 -r, --limitoutput, --limit-output
     LimitOutput - Limit the output to essential information

     --timeout, --execution-timeout=VALUE
     CommandExecutionTimeout (in seconds) - The time to allow a command to
       finish before timing out. Overrides the default execution timeout in the
       configuration of 2700 seconds. '0' for infinite starting in 0.10.4.

 -c, --cache, --cachelocation, --cache-location=VALUE
     CacheLocation - Location for download cache, defaults to %TEMP% or value
       in chocolatey.config file.

     --allowunofficial, --allow-unofficial, --allowunofficialbuild, --allow-unofficial-build
     AllowUnofficialBuild - When not using the official build you must set
       this flag for choco to continue.

     --failstderr, --failonstderr, --fail-on-stderr, --fail-on-standard-error, --fail-on-error-output
     FailOnStandardError - Fail on standard error output (stderr), typically
       received when running external commands during install providers. This
       overrides the feature failOnStandardError.

     --use-system-powershell
     UseSystemPowerShell - Execute PowerShell using an external process
       instead of the built-in PowerShell host. Should only be used when
       internal host is failing. Available in 0.9.10+.

     --no-progress
     Do Not Show Progress - Do not show download progress percentages.
       Available in 0.10.4+.

     --proxy=VALUE
     Proxy Location - Explicit proxy location. Overrides the default proxy
       location of ''. Available for config settings in 0.9.9.9+, this CLI
       option available in 0.10.4+.

     --proxy-user=VALUE
     Proxy User Name - Explicit proxy user (optional). Requires explicity
       proxy (`--proxy` or config setting). Overrides the default proxy user of
       ''. Available for config settings in 0.9.9.9+, this CLI option available
       in 0.10.4+.

     --proxy-password=VALUE
     Proxy Password - Explicit proxy password (optional) to be used with
       username. Requires explicity proxy (`--proxy` or config setting) and
       user name.  Overrides the default proxy password (encrypted in settings
       if set). Available for config settings in 0.9.9.9+, this CLI option
       available in 0.10.4+.

     --proxy-bypass-list=VALUE
     ProxyBypassList - Comma separated list of regex locations to bypass on
       proxy. Requires explicity proxy (`--proxy` or config setting). Overrides
       the default proxy bypass list of ''. Available in 0.10.4+.

     --proxy-bypass-on-local
     Proxy Bypass On Local - Bypass proxy for local connections. Requires
       explicity proxy (`--proxy` or config setting). Overrides the default
       proxy bypass on local setting of 'True'. Available in 0.10.4+.

     --log-file=VALUE
     Log File to output to in addition to regular loggers. Available in 0.1-
       0.8+.
Chocolatey v0.10.11

C:\Windows\system32>
```
### 2 C:\Windows\system32> choco install spf13-vim      管理员身份
```shell
Windows PowerShell
版权所有 (C) Microsoft Corporation。保留所有权利。

PS C:\Windows\system32> choco install spf13-vim
Chocolatey v0.10.11
Installing the following packages:
spf13-vim
By installing you accept licenses for the packages.
Progress: Downloading vim 8.0.604... 100%
Progress: Downloading spf13-vim 3.0.3... 100%
Progress: Downloading curl 7.62.0... 100%
Progress: Downloading git 2.19.1... 100%
Progress: Downloading git.install 2.19.1... 100%
Progress: Downloading chocolatey-core.extension 1.3.3... 100%
Progress: Downloading ctags 5.8.1... 100%

vim v8.0.604 [Approved]
vim package files install completed. Performing other installation steps.
The package vim wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Downloading vim
  from 'https://sourceforge.net/projects/cream/files/Vim/8.0.604/gvim-8-0-604.exe/download'
Progress: 100% - Completed download of C:\Users\lx\AppData\Local\Temp\chocolatey\vim\8.0.604\gvim-8-0-604.exe (9.22 MB).
Download of gvim-8-0-604.exe (9.22 MB) completed.
Installing vim...
vim has been installed.
Adding the vim installation directory to PATH …
PATH environment variable does not have C:\Program Files (x86)\vim\vim80 in it. Adding...
  vim may be able to be automatically uninstalled.
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of vim was successful.
  Software installed as 'exe', install location is likely default.

curl v7.62.0 [Approved]
curl package files install completed. Performing other installation steps.
The package curl wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint):

Timeout or your choice of '' is not a valid selection.
You must select an answer
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Extracting 64-bit C:\ProgramData\chocolatey\lib\curl\tools\curl-7.62.0-win64-mingw.zip to C:\ProgramData\chocolatey\lib\curl\tools...
C:\ProgramData\chocolatey\lib\curl\tools
 ShimGen has successfully created a shim for curl.exe
 The install of curl was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\curl\tools'

chocolatey-core.extension v1.3.3 [Approved]
chocolatey-core.extension package files install completed. Performing other installation steps.
 Installed/updated chocolatey-core extensions.
 The install of chocolatey-core.extension was successful.
  Software installed to 'C:\ProgramData\chocolatey\extensions\chocolatey-core'

git.install v2.19.1 [Approved]
git.install package files install completed. Performing other installation steps.
The package git.install wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Using Git LFS
Installing 64-bit git.install...
git.install has been installed.
git.install installed to 'C:\linuix\Git'
  git.install can be automatically uninstalled.
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of git.install was successful.
  Software installed to 'C:\linuix\Git\'

git v2.19.1 [Approved]
git package files install completed. Performing other installation steps.
 The install of git was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

ctags v5.8.1
ctags package files install completed. Performing other installation steps.
The package ctags wants to run 'ChocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

WARNING: Url has SSL/TLS available, switching to HTTPS for download
Downloading ctags
  from 'https://sourceforge.net/projects/ctags/files/ctags/5.8/ctags58.zip'
Progress: 100% - Completed download of C:\Users\lx\AppData\Local\Temp\chocolatey\ctags\5.8.1\ctags58.zip (558.45 KB).
Download of ctags58.zip (558.45 KB) completed.
Extracting C:\Users\lx\AppData\Local\Temp\chocolatey\ctags\5.8.1\ctags58.zip to C:\Users\lx\AppData\Local\Temp\chocolatey\chocolatey\ctags...
C:\Users\lx\AppData\Local\Temp\chocolatey\chocolatey\ctags
 ShimGen has successfully created a shim for ctags.exe
 The install of ctags was successful.
  Software installed to 'C:\Users\lx\AppData\Local\Temp\chocolatey\chocolatey\ctags'

spf13-vim v3.0.3 [Approved]
spf13-vim package files install completed. Performing other installation steps.
The package spf13-vim wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

#< CLIXML
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><Obj S="progress" RefId="0"><TN RefId="0"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>正在准备首次使用模块。</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><Obj S="progress" RefId="1"><TNRef RefId="0" /><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>正在准备首次使用模块 。</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><S S="debug">Host version is 5.1.17763.1, PowerShell Version is '5.1.17763.1' and CLR Version is '4.0.30319.42000'.</S><S S="verbose">正在导 出函数“Format-FileSize”。</S><S S="verbose">正在导出函数“Get-ChecksumValid”。</S><S S="verbose">正在导出函数“Get-ChocolateyUnzip”。</S><S S="verbose">正在导出函数“Get-ChocolateyWebFile”。</S><S S="verbose">正在导出函数“Get-EnvironmentVariable”。</S><S S="verbose">正在导出函数“Get-EnvironmentVariableNames”。</S><S S="verbose">正在导出函数“Get-FtpFile”。</S><S S="verbose">正在导出函数“Get-OSArchitectureWidth”。</S><S S="verbose">正在导出函数“Get-PackageParameters”。</S><S S="verbose">正在导出函数“Get-PackageParametersBuiltIn”。</S><S S="verbose">正在导出函数“Get-ToolsLocation”。</S><S S="verbose">正在导出函数“Get-UACEnabled”。</S><S S="verbose">正在导出函数“Get-UninstallRegistryKey”。</S><S S="verbose">正在导出函数“Get-VirusCheckValid”。</S><S S="verbose">正在导出函数“Get-WebFile”。</S><S S="verbose">正在导出函数“Get-WebFileName”。</S><S S="verbose">正在导出函数“Get-WebHeaders”。</S><S S="verbose">正在导出函数“Install-BinFile”。</S><S S="verbose">正在导出函数“Install-ChocolateyDesktopLink”。</S><S S="verbose">正在导出函数“Install-ChocolateyEnvironmentVariable”。</S><S S="verbose">正在导出函数“Install-ChocolateyExplorerMenuItem”。</S><S S="verbose">正在导出函数“Install-ChocolateyFileAssociation”。</S><S S="verbose">正在导出函数“Install-ChocolateyInstallPackage”。</S><S S="verbose">正在导出函数“Install-ChocolateyPackage”。</S><S S="verbose">正在导出函数“Install-ChocolateyPath”。</S><S S="verbose">正在导出函数“Install-ChocolateyPinnedTaskBarItem”。</S><S S="verbose">正在导出函数“Install-ChocolateyPowershellCommand”。</S><S S="verbose">正在导出函数“Install-ChocolateyShortcut”。</S><S S="verbose">正在导 出函数“Install-ChocolateyVsixPackage”。</S><S S="verbose">正在导出函数“Install-ChocolateyZipPackage”。</S><S S="verbose">正在导出函数“Install-Vsix”。</S><S S="verbose">正在导出函数“Set-EnvironmentVariable”。</S><S S="verbose">正在导出函数“Set-PowerShellExitCode”。</S><S S="verbose">正在导出函数“Start-ChocolateyProcessAsAdmin”。</S><S S="verbose">正在导出函数“Test-ProcessAdminRights”。</S><S S="verbose">正在导出函数“Uninstall-BinFile”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyEnvironmentVariable”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyPackage”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyZipPackage”。</S><S S="verbose">正在导出函数“Update-SessionEnvironment”。</S><S S="verbose">正在导出函数“Write-ChocolateyFailure”。</S><S S="verbose">正在导出函数“Write-ChocolateySuccess”。</S><S S="verbose">正在导出函数“Write-FileUpdateLog”。</S><S S="verbose">正在导出函数“Write-FunctionCallLogMessage”。</S><S S="verbose">正在导出别名“Get-ProcessorBits”。</S><S S="verbose">正在导出别名“Get-OSBitness”。</S><S S="verbose">正在导出别名“Get-InstallRegistryKey”。</S><S S="verbose">正在导出别名“Generate-BinFile”。</S><S S="verbose">正在导出别名“Add-BinFile”。</S><S S="verbose">正在导出别名“Start-ChocolateyProcess”。</S><S S="verbose">正在导出别名“Invoke-ChocolateyProcess”。</S><S S="verbose">正在导出别名“Remove-BinFile”。</S><S S="verbose">正在导出别名“refreshenv”。</S><S S="debug">Loading community extensions</S><S S="debug">Importing 'C:\ProgramData\chocolatey\extensions\chocolatey-core\chocolatey-core.psm1'</S><S S="verbose">正在从路径“C:\ProgramData\chocolatey\extensions\chocolatey-core\chocolatey-core.psm1”加载模块。</S><S S="verbose">正在导出函数“Get-UninstallRegistryKey”。</S><S S="verbose">正在导出 函数“Get-AppInstallLocation”。</S><S S="verbose">正在导出函数“Get-AvailableDriveLetter”。</S><S S="verbose">正在导出函数“Get-EffectiveProxy”。</S><S S="verbose">正在导出函数“Get-PackageCacheLocation”。</S><S S="verbose">正在导出函数“Get-PackageParameters”。</S><S S="verbose">正在导出函数“Get-WebContent”。</S><S S="verbose">正在导出函数“Register-Application”。</S><S S="verbose">正在导入函数“Get-AppInstallLocation”。</S><S S="verbose">正在导入函数“Get-AvailableDriveLetter”。</S><S S="verbose">正在导入函数“Get-EffectiveProxy”。</S><S S="verbose">正在导入函数“Get-PackageCacheLocation”。</S><S S="verbose">正在导入函数“Get-PackageParameters”。</S><S S="verbose">正在导入函数“Get-UninstallRegistryKey”。</S><S S="verbose">正在导入函数“Get-WebContent”。</S><S S="verbose">正在导入函数“Register-Application”。</S><S S="verbose">正在导出函数“Format-FileSize”。</S><S S="verbose">正在导出函数“Get-ChecksumValid”。</S><S S="verbose">正在导出函数“Get-ChocolateyUnzip”。</S><S S="verbose">正在导出函数“Get-ChocolateyWebFile”。</S><S S="verbose">正 在导出函数“Get-EnvironmentVariable”。</S><S S="verbose">正在导出函数“Get-EnvironmentVariableNames”。</S><S S="verbose">正在导出函数“Get-FtpFile”。</S><S S="verbose">正在导出函数“Get-OSArchitectureWidth”。</S><S S="verbose">正在导出 函数“Get-PackageParameters”。</S><S S="verbose">正在导出函数“Get-PackageParametersBuiltIn”。</S><S S="verbose">正在 导出函数“Get-ToolsLocation”。</S><S S="verbose">正在导出函数“Get-UACEnabled”。</S><S S="verbose">正在导出函数“Get-UninstallRegistryKey”。</S><S S="verbose">正在导出函数“Get-VirusCheckValid”。</S><S S="verbose">正在导出函数“Get-WebFile”。</S><S S="verbose">正在导出函数“Get-WebFileName”。</S><S S="verbose">正在导出函数“Get-WebHeaders”。</S><S S="verbose">正在导出函数“Install-BinFile”。</S><S S="verbose">正在导出函数“Install-ChocolateyDesktopLink”。</S><S S="verbose">正在导出函数“Install-ChocolateyEnvironmentVariable”。</S><S S="verbose">正在导出函数“Install-ChocolateyExplorerMenuItem”。</S><S S="verbose">正在导出函数“Install-ChocolateyFileAssociation”。</S><S S="verbose">正在导出函数“Install-ChocolateyInstallPackage”。</S><S S="verbose">正在导出函数“Install-ChocolateyPackage”。</S><S S="verbose">正在导 出函数“Install-ChocolateyPath”。</S><S S="verbose">正在导出函数“Install-ChocolateyPinnedTaskBarItem”。</S><S S="verbose">正在导出函数“Install-ChocolateyPowershellCommand”。</S><S S="verbose">正在导出函数“Install-ChocolateyShortcut” 。</S><S S="verbose">正在导出函数“Install-ChocolateyVsixPackage”。</S><S S="verbose">正在导出函数“Install-ChocolateyZipPackage”。</S><S S="verbose">正在导出函数“Install-Vsix”。</S><S S="verbose">正在导出函数“Set-EnvironmentVariable”。</S><S S="verbose">正在导出函数“Set-PowerShellExitCode”。</S><S S="verbose">正在导出函数“Start-ChocolateyProcessAsAdmin”。</S><S S="verbose">正在导出函数“Test-ProcessAdminRights”。</S><S S="verbose">正在导出函数“Uninstall-BinFile”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyEnvironmentVariable”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyPackage”。</S><S S="verbose">正在导出函数“Uninstall-ChocolateyZipPackage”。</S><S S="verbose">正在导出函数“Update-SessionEnvironment”。</S><S S="verbose">正在导出函数“Write-ChocolateyFailure”。</S><S S="verbose">正在导出函数“Write-ChocolateySuccess”。</S><S S="verbose">正在导出函数“Write-FileUpdateLog”。</S><S S="verbose">正在导出函数“Write-FunctionCallLogMessage”。</S><S S="verbose">正在导出函数“Get-AppInstallLocation”。</S><S S="verbose">正在导出函数“Get-AvailableDriveLetter”。</S><S S="verbose">正在导出函数“Get-EffectiveProxy”。</S><S S="verbose">正在导出函数“Get-PackageCacheLocation”。</S><S S="verbose">正在导出函数“Get-WebContent”。</S><S S="verbose">正在导出函数“Register-Application”。</S><S S="verbose">正在导出别名“Get-ProcessorBits”。</S><S S="verbose">正在导出别名“Get-OSBitness”。</S><S S="verbose">正在导出别名“Get-InstallRegistryKey”。</S><S S="verbose">正在导出别名“Generate-BinFile”。</S><S S="verbose">正在导出别名“Add-BinFile”。</S><S S="verbose">正在导出别名“Start-ChocolateyProcess”。</S><S S="verbose"> 正在导出别名“Invoke-ChocolateyProcess”。</S><S S="verbose">正在导出别名“Remove-BinFile”。</S><S S="verbose">正在导出别名“refreshenv”。</S><Obj S="information" RefId="2"><TN RefId="1"><T>System.Management.Automation.InformationRecord</T><T>System.Object</T></TN><ToString>-= Installing spf13-vim =-</ToString><Props><Obj N="MessageData" RefId="3"><TN RefId="2"><T>System.Management.Automation.HostInformationMessage</T><T>System.Object</T></TN><ToString>-= Installing spf13-vim =-</ToString><Props><S N="Message">-= Installing spf13-vim =-</S><B N="NoNewLine">false</B><S N="ForegroundColor">DarkYellow</S><S N="BackgroundColor">DarkMagenta</S></Props></Obj><S N="Source">C:\ProgramData\chocolatey\lib\spf13-vim\tools\spf13-vim-windows-install.ps1</S><DT N="TimeGenerated">2018-11-09T14:24:02.8050678+08:00</DT><Obj N="Tags" RefId="4"><TN RefId="3"><T>System.Collections.Generic.List`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]</T><T>System.Object</T></TN><LST><S>PSHOST</S></LST></Obj><S N="User">DESKTOP-32BH6EU\lx</S><S N="Computer">DESKTOP-32BH6EU</S><U32 N="ProcessId">10164</U32><U32 N="NativeThreadId">1972</U32><U32 N="ManagedThreadId">9</U32></Props></Obj><Obj S="information" RefId="5"><TNRef RefId="1" /><ToString>Checking for installation dependencies:</ToString><Props><Obj N="MessageData" RefId="6"><TNRef RefId="2" /><ToString>Checking for installation dependencies:</ToString><Props><S N="Message">Checking for installation dependencies:</S><B N="NoNewLine">false</B><S N="ForegroundColor">DarkYellow</S><S N="BackgroundColor">DarkMagenta</S></Props></Obj><S N="Source">C:\ProgramData\chocolatey\lib\spf13-vim\tools\spf13-vim-windows-install.ps1</S><DT N="TimeGenerated">2018-11-09T14:24:02.8315157+08:00</DT><Obj N="Tags" RefId="7"><TNRef RefId="3" /><LST><S>PSHOST</S></LST></Obj><S N="User">DESKTOP-32BH6EU\lx</S><S N="Computer">DESKTOP-32BH6EU</S><U32 N="ProcessId">10164</U32><U32 N="NativeThreadId">1972</U32><U32 N="ManagedThreadId">9</U32></Props></Obj><S S="warning">Could not install spf13-vim!</S><S S="warning">Git not found! The git commandline must be installed before running this script</S></Objs>
0
WARNING: Write-ChocolateySuccess is deprecated and will be removed in v2. If you are the maintainer, please remove it from your package file.
Only an exit code of non-zero will fail the package by default. Set
 `--failonstderr` if you want error messages to also fail a script. See
 `choco -h` for details.
 The install of spf13-vim was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

Chocolatey installed 7/7 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

Installed:
 - spf13-vim v3.0.3
 - chocolatey-core.extension v1.3.3
 - ctags v5.8.1
 - git.install v2.19.1
 - vim v8.0.604
 - curl v7.62.0
 - git v2.19.1
PS C:\Windows\system32>
```
