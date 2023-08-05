import hashlib
from base64 import b64encode

# noinspection PyCompatibility
from collections import Mapping

import boto3
from moto import mock_kms

from config_yourself import Config

test_kms_region_name = "us-east-1"

CONFIG_TEMPLATE = u"""crypto:
  key: {}
  region: {}
  provider: kms
{}
"""

KEYS = {
    "kms": "arn:aws:kms:us-east-1:000000000000:key/00000000-0000-0000-0000-000000000000",
    "password": "dRVeKIGwNwJU0LQ69eUwsUyQRCyPh7DMRiU1bK//LtoMg81SHohquBR9S5fSYa6Uz+yvAHrx2KjBzS+0QXs6bM6fDJVpNodXOgA5XtNMV+iA8hVZlkC12cnfsNw=",
    "gpg": """-----BEGIN PGP MESSAGE-----

hQEMA1XMevbqrQGfAQf/avgPH4FgUhg8Y6+wLwrrb1DnrEFRKalEDtvtfjbPTWAL
eSAHi92R/CbQQFhO3w1WaaSJf9YLguJcMyvu1e0uquvk+dvvvGScnPIjSTmMyKY+
8kFvXCPlpijbTSWj9LsFr+TwYmtZx34e/OEZwu8g2T0TlFG17R9m/PBk9Dh1DSQF
LMsUyX9BeV9A5gNRywjyc4kymXTjnUHaqASkGe863Mb4mL0ySf2oijjvEoYuqypB
ya34fx+QNe3XMrvk8QCYlDc3Eim5y88kFoyhTsa3uvf1DCQ0vOEFPsjgtODQclaD
UDIsxleW1bYvJRIRSuixojJUv/Stl/uBrxjd8RPPyNJeAS2vf6z7Z8oIkVfMTByI
L0lvkKAktk+tx3B/ePo4YnF51B00XzL5AmVB2skmYkKT7zV3XWVWFggY/hwctn/0
CV1qjwbNI3Sl1qUvyvSV8zCMLozHpzXNocRpVXVyag==
=A9X2
-----END PGP MESSAGE-----
""",
}


def add_kms_entries(config):
    if isinstance(config, Mapping):
        dict_with_kms_entries = config.copy()

        dict_with_kms_entries["crypto"] = dict(
            key=KEYS["kms"], region=test_kms_region_name, provider="kms"
        )
        return dict_with_kms_entries
    else:
        return CONFIG_TEMPLATE.format(KEYS["kms"], test_kms_region_name, config)


@mock_kms
def get_config_yourself(*config, **kwargs):
    return Config(*config, **kwargs)


@mock_kms
def encrypt_test_value(plaintext):
    kms_client = boto3.client("kms", region_name="us-east-1")
    kms_response = kms_client.encrypt(
        KeyId=KEYS["kms"], Plaintext=plaintext.encode("utf-8")
    )
    return {
        "encrypted": True,
        "ciphertext": b64encode(kms_response["CiphertextBlob"]).decode("utf-8"),
        "hash": b64encode(hashlib.sha256(plaintext.encode("utf-8")).digest()).decode(
            "utf-8"
        ),
    }


SECRETS = {}
SECRETS["password"] = {"password": "password"}
SECRETS["gpg"] = {}
SECRETS["gpg"][
    "privateKey"
] = """-----BEGIN PGP PRIVATE KEY BLOCK-----

lQcYBFvKJt0BEAD4QOSlXEuXIR6oqqJH3SWqo//RrmhwU6eFIm24ZVUTFghXD+gC
1rp9LNuuFVX5JuLr1WEdCHpm5k1mzR6fAoV+sWypKckBsGkeHNJcErZ2Lm8/VoeF
B5u+el6G65/hTCsSwyu02/tCFt/IqxGfM+qaSav2lzRfwEgtB5vP0gJ4BSmhIcrY
VJl9nUrp1WL3TZMKDugBKoejiNNo43WH3KGhAkCFNXS3s+8enBGZ4XYhAGjvi1Rn
r7TYD8F5zrZk39qKw9mIrgtTBvszTN2SO9mEJCkdlT05e7+mV6oRpWq/oTaptaG4
Dy/vmZmB67Cpf7RrEzYIoh3eOlmX1lSQpW3mx7r6APFTq9eYv03ywyc2Hfbk36RT
Ch+LJ/WW8EobVznVVryFAWy1sP41XhBwsr2ogPTYKWlGvGRnTX7p5OMhmZ8JJiAt
Voo49fDCyNQNxBkZlIeu1CdfOfKuJE2E3QfrAcSdlgLU3fawRAcX7TdAhgX7HSbi
z4O/QfeaQy8hSXbw1yfUvVZWw6aqQ+tcJAxU2Z3/cv6lIRPvXbIgyiWQig22h8YZ
Ab0/wWcNRNbWv3ge6UYEV1CmE+AOjHn3/NmSglHir2xKd0FAW5g0EziVUZpFGeq8
Q2PLF1XhtnAML16eO5+92KMSmWLwJF5Sito0ddFAGtF/EhlI5YvgwBKfywARAQAB
AA//aaUoCEzmKCrigrGWvNFaMat39tHrRP38mLYFjkalNSmXpAEzYV3i39kipYsT
2qMXR3g3SyUr/bU9NCXPRajLiZZUoQqUrUDXAwcN6DvYZSOumPwoUM7jkuQ9bNpB
4B1LaUEgTOeencnhMuLF7YOo7z6xzQ8crTDFJlCKGJ8NCOldhWI9keEyrpes5SS3
aHmdPNcKGVDxhwD3wrelcQtNxxiPv4B3qqOKe3K8NMmTPUkQ3vvij/tgkN/nnIAA
852lwY7F+JnkXNFoPjUUR6JrlwXSb3Huq5NDhDTjPX4xFtqyyfbvGsZvxl2Ny5Gy
zPb5HuX+hR8EaelX7js6IpIb2ZcN6SJuSNnYcJpwuyv24V2Xpwr742UH2zR8xWx6
IBJCzjp2PZHhpVYOPOnQQb1kX7fpay+uWb0EIBenNR0CaVin5gunxzsV7xivkIiH
V0C+S4Im88ojUcbLFDd8Tf4+lmFumoyhIhVb0IuBTETJ7e63vnq6d/7ct8AQngNG
pcztoR6P1mrN4HtGVGrCUM2KWVnRnjI0+GU/uYLabUwku4cg66WbOERMZ7Htj1h5
/4GpsoW2Ue/TYhwlMHumeoX+HOQLtueJohC08sxr6oIwi/B1Jvzks6QiZiF/ATyQ
sKOuj5dp1S/QJKw1+T04nwfXoCEVuEP07/5JExP0XehWAukIAPtmGPGFXB+aUMLO
mgb8JtTVQjhbX+1T1sYKNSbcbEYqMwlIC5PJ3JKCK+e/rVewzhHhk42MxlWJaELi
FbkmENqrQGXTC50S4zXlT2Mh4kup7AWJ5EmBTxvCXmkSFAdU9NkTdWw8uStnbdWl
ryM0timtl2+1DZYZBMJ2RsPtvW8c+FQaUh13sGXmHs6QsMtMpzIIgCodQimBqbhH
WWsNi5XAUC0Mu+hxKnWdHGqlKIFMfwahA3IVzSzHukMra7kEC5cYR2iMn1BGfhAH
DlEfkluI+EJQtu/Vwt+3RhNHs3DHDqNJKYtVM2+SyO/b2HIN/CPW7OQThZW6FcGT
ZN++ZGMIAPzMDwDEoTZ3pZh/WaWEseu/cgtcS7IqJDVFyssSMN+pDs+ErNR7LcDB
mKjzSGjgoJ8UooFdlnXYnQBwfvf34bddD9MGDfe+pUR4SP5eQuBXT17E+SNsoCoK
TQAAbbtWBIKg+W4qX7p0XZyx689+G3P/hl2Sx3dljhikGbO1M6qphCf4GakPVBjp
JrjFu8rViz2e9fCP9m1QoB57B2r4pfTonGjl1mVHshXh4Jrh/hqeMjbo80W3qj7E
K26GFZfufGvN/KMWH12RQSpBDlm+q3wJElWVMmbafKCZdy1otWBaaEkwC2rmK9Li
xyhzG91gIcnKB9tGd8wQZN4v6untL3kIAMt0fSqziydsiA2QjWMeaTui2VVyrwT2
D4PUnrFIJAB5asOKAh7Dna+8rOYrPOWTibemdlI9hn6sZPvRK1JCWysQQs+4JaH5
PLhA8fRxWR/Yz5pI09Ef6ZynSGbGZdXaooj6sJRuTUhmD9P2DPPS+jBd1ADFmLZi
X5WSOKThYKy1v+TCCYcperOzO9uXLgSyplYjYHreS4yH8SeAnO3vWt2pZzQK6bUf
b0HqPsR4ctgnWnCKVNNMSeLI80OLRiN58Vytcq+muVIzidCADpPN22DlYUYKrJHu
3AORIjIy5nkeGfpY7boXjzTq/ygp7ESPA9N7BBQXuIuZJJYxt9jG11WA1LQ8VGVz
dCBzb2Z0d2FyZSAoYmxpbmstY29uZmlnKSA8dGVzdC1zb2Z0d2FyZUBibGlua2hl
YWx0aC5jb20+iQJOBBMBCgA4FiEE0HewJndVBgqt4umJJI8ZE+xgBvsFAlvKJt0C
Gy8FCwkIBwMFFQoJCAsFFgIDAQACHgECF4AACgkQJI8ZE+xgBvutUw/+OKHhmZdg
FMXB67zu6Mk+S99MV+v7ftEJRcSD6tYz2d/vukVzvIGbNrnaZuBCpz+kIGcwyUfb
fJc2q+aF+ZvUpvFnwvMPHTtVxEjX8i7U+znFn4HRn9h0RohpJU9Gl8wCisl6FWX7
e15mE5JzKIIZ1QMeG0iFIlgFTele6/jAzz53BKHHILOj22WFY++u/ebk6h7K0Qqu
ppn3Cefvn3SAVyv88UB4bSVhbtUMeHUy7ykzaatCFneuIGnMMU0FtFGCH5jwDyIK
wztmapM9vb5o8Mp5Ad2WfD8C0xC5wwNvV0vd8jPtQ63EAluBV98FKq740srhCg8I
OLIj+ZDDFB85dHzDAbFvWNkJznlC5vRhSI1Quuj8H9e5E7VOeUdaBfcB5Xr3p6c+
9PiIugUSbfVqcooYmtcOEgpvyMXMdgt9XtdfdUwu4p5+nUm5V1mtnzG+MQRyVOdo
gQBZFnKvYe4az0Stm6M3hlbeNBC3prXxBA8yYQZDrKb2Xov0m/QqpK8cXTd/vWlo
gKUy3NxmcYRgCZVjSogM1AE/pkhJ7v6iCPQpzynnsTYiX2hZz1BJlvhhpESAlTfG
NjmFkSXVszyVEd5s59eg3cEFBW+B87fi72j5cI0jGU8HK6iG6rY/gcve9VOS/6DG
TtqZU8OGbHMjG1T78dE93DyMQqGH0XMhfpOdA5gEW8om3QEIAKkSdas1KARBKt1A
CaLw4nvwZYCtOQLL/WawmQ4xzfaWqmiaMVZVHlrPHbCsDi21YsZp/tJ3QcDqaff4
ACmcqYvPge1AoVLlWUElQduDBUPiWmvXfnFQ2OIrZpsEpG2rrdMhqHMigN7nnc2l
8wQQFs01I2NdxpMmGVAc0QL/uFv6Nal2WRiq3NxAfPA7EmJuh/5TTtT+lIsfjIvH
t97Lar8upgAt1YuIHKNfWe/iduK9/xAqiFtEisa6HJvXaQZ4xN6C+1JTPFi6Jh//
RwVqrV6r0uFBrZ/Ve4lfxx5ehHLL08+sLSibrj6ZcFIjHMqjSND7l//XmuseXr3g
wj/Lol0AEQEAAQAH/AmYyqUVN1hGerBkWietlK2ET76mFn5aJeAWVhnAKfi9RJ77
YaGM41Q0PXMx0Pw3N4wbqCM6MblJlQpGQXwbMGSHOtDEwmN6MT7JZpuXLE1WI9vL
N5onBKiR3hkeglbXT96UIoOmibodW4+4w7qPTzwGsCOLxyHDH9y0RgjtiwFtcs8W
ni45HXGRtmpnRvuyyyD/H3q7QfIJJXWKH+Xjm/kkmjn6Kk0ejGeMbGpi+Gmps2S4
r/9Sr5AYsfjCybgAulPRu7rFuA1V5CkS+oi5AEGbPwlrCEttTI+7j8T/Ly3XI9dS
IlE9holfvkGWwlcKFj2Lvrr/RXAGnWMhfAQk3AEEAMxkBJfDWNFU774z9RVrjk17
rd8Z36744g6rhgR/5PxqfTF76tppca7jNozqmmZTKArb57QnvyMhWWHQON4F/k3c
ZXFlTZWLe81k9L5y94HLeD/ZyaFY57Vt1v0cxVU8CavdforNdO98aGD+blYcuK8i
OVtS9Z3R69l632qaUOUhBADTw2tWMiJyS11okX1/PKwCGDzNMdk1CPGNYalgygN7
N3medItbhscL4slI+TZBPWkDLV+uw5PLpwL+9jvTexR0fkHnwfr/OmQ7EqLIuvJG
7CXEQa773fET8AiMTr7iV+gHBQkvnK0XeIm4zQejC8DyWDAM3Xe0edAm/+rUOypZ
vQP9EZSSFT9hfNZ32aa9WqmABXiJDkPqDJyU8A2z/BMCDurKsN0xeicRlG7LUGLd
KzS3ehw+ZaaH1PeRKifsud2sJaHPeM8BRW3eDSLdP3sqBZ/7a09d2EaILSj879Je
+U9lgROc9+0HgJt3x0p48tG/lXXSk+9RC94oQ5DcfJnwyE8+rIkCNgQYAQoAIBYh
BNB3sCZ3VQYKreLpiSSPGRPsYAb7BQJbyibdAhsMAAoJECSPGRPsYAb7Tp8P/2td
RWm1b/QBVzeYOlR3tcUN499y1b5ywGt1mfhYOYVSi/HjOgZooo/nifXUcY3oMIsX
ZhWzWfMZkxPAMqmZlUEdBiYPzj8rQF+VNN1uGK2sQ0gsl4B+nqNtbgwQfu4gDoJr
+evh0iVPzIum/0ezVj2h9lsAcQVRv9psw1hWypLhGHGy3UU/3KHK2xSteRJaPn7Z
P4WfMKCFouDN/E+eDkFygdkJxt2vVrdqwnrbQAY4yRjuLA/0l67VZ9t+n1s07j1A
DZLp2i/5XsEPamZKNT0agb91M8gZbiFBxPsz7NT/gMziYek2HYdnWO8KnSomFgOC
U0M3T4j92SIliYI228dQ9vGWouTvqdaceOc4peSkvlctYGF5itE/SOKX+DFk4NOI
1DaJ20rWv3TYBEgYNrYQ4ahaSZsiejj+oxCDHQ2KcbKHpCpYJVBNUKIoYpy/lEFt
577lhFSiIdYxGV+mbeZFT80MuzlYfJnCfsmNs8cCSdcT2deYQmPRM85Te0IljWhn
o2PFENM6s0fXRdFY4j9zzx9ijaxzXJ+E9szgyvLDKsbGvZaqs/cEXtG1ux87zgVv
Ai07s0JfSJbEn6hWCtcn8Hz/iDrF2GfoBGBCusOIufDNQbp87I8ISllbdBd+Dfv3
4DjkMu6uv8gq2f6a9yu1QtdzbaX+XE4wkCBMENnI
=if4J
-----END PGP PRIVATE KEY BLOCK-----
"""
