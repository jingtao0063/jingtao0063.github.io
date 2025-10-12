import base64
import json
import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

def decrypt_vault():
    # 获取加密的vault.json内容
    encrypted_base64 = input("请输入vault.json的加密内容: ").strip()
    
    # 获取主密码
    master_password = getpass.getpass("请输入主密码: ")
    
    try:
        # 派生密钥
        key = SHA256.new(master_password.encode('utf-8')).digest()
        
        # Base64解码
        encrypted_data = base64.b64decode(encrypted_base64)
        
        # 分离IV和密文
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        
        # 创建AES解密器
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # 解密数据
        decrypted_padded = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted_padded, AES.block_size).decode('utf-8')
        
        # 解析JSON
        passwords = json.loads(decrypted)
        
        print("\n解密成功! 密码数据:")
        print(json.dumps(passwords, indent=2))
        
        # 询问是否保存到文件
        save_file = input("\n是否保存到文件? (y/n): ").lower()
        if save_file == 'y':
            filename = input("输入文件名 (默认: passwords.json): ") or "passwords.json"
            with open(filename, 'w') as f:
                json.dump(passwords, f, indent=2)
            print(f"数据已保存到 {filename}")
            
    except Exception as e:
        print(f"解密失败: {str(e)}")

if __name__ == "__main__":
    print("SecurePass 密码库解密工具")
    print("=" * 40)
    decrypt_vault()