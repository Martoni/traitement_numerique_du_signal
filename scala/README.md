# installation d'ammonite

Pour avoir la [console en direct](https://ammonite.io/#InstallationonLinux) :

```
$ sudo sh -c '(echo "#!/usr/bin/env sh" && curl -L https://github.com/com-lihaoyi/Ammonite/releases/download/2.5.4/2.13-2.5.4) > /usr/local/bin/amm && chmod +x /usr/local/bin/amm' && amm
```

Pour importer [spire](https://typelevel.org/spire/)

```
@ import $ivy.`org.typelevel::spire:0.18.0`
@ import spire._
@ import spire.math._
@ import sipre.implicits._
@ Complex(3.0,5.0).sin
res: Complex[Double] = Complex(real = 10.472508533940392, imag = -73.46062169567367)
```
