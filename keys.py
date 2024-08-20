from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip44, Bip44Coins, Bip44Changes

# Step 1: Generate a BIP39 mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)  # Generate a 12-word mnemonic
print("Mnemonic:", mnemonic)

# Step 2: Generate a seed from the mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Step 3: Generate the Bitcoin account using BIP44 standard (P2PKH address)
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

# Derive the key (account 0, external chain)
bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

# Get the address (P2PKH)
bitcoin_address = bip44_acc_ctx.PublicKey().ToAddress()

# Get the private and public keys
private_key = bip44_acc_ctx.PrivateKey().ToWif()  # WIF format private key
public_key = bip44_acc_ctx.PublicKey().RawCompressed().ToHex()  # Hex format public key

# Print results
print("Mnemonic:", mnemonic)
print("Bitcoin Address (P2PKH):", bitcoin_address)
print("Private Key (WIF):", private_key)
print("Public Key (Hex):", public_key)
