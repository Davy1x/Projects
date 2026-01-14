const { ZeusZ8Engine } = require('./modules/zeus_z8engine.js');
const { metadata, encryption_key, decryption_key } = ZeusZ8Engine;


class ZeusEncryptZ8Engine {
  constructor({ Data = "ZeusZ8Engine", Decrypt = false, Encrypt = false, AllowMetadata = false, AllPackages = false }) {
    this.data = Data;
    this.decrypt = Decrypt;
    this.encrypt = Encrypt;
    this.allPackages = AllPackages;
    this.allowMetadata = AllowMetadata;
    return this.ZeusEncryptDecrypt();
  }
  ZeusEncryptDecrypt() {
    let decrypting = Array();
    let encrypting = Array();
    let Encrypto = { data: {} };
    if (this.encrypt && !this.decrypt) {
      try {
        for (let chars of this.data) {
          for (let [key, value] of Object.entries(encryption_key)) {
            if (chars === key) {
              decrypting.push(chars);
              encrypting.push(value);
            }
          }
        }
        this.allowMetadata ? Encrypto.metadata = { ...metadata } : null;
        this.allowMetadata ? Encrypto.metadata.encryption_time = Date() : null;
        if (this.allPackages) {
          Encrypto.data.encrypt = encrypting.join(String());
          Encrypto.data.decrypt = decrypting.join(String());
          return Encrypto;
        }
        this.encrypt ? Encrypto.data = encrypting.join(String()) : null;
        return Encrypto
      } catch (err_exception) {
        return ({ EXCEPTION: err_exception });
      }
    } else if (this.decrypt && !this.encrypt) {
      try {
        const zeusArr = ()=>{
          let temp = Array();
          for (let x = 0; x < this.data.length; x += 4) {
            temp.push(this.data.substring(x, x + 4))
          }
          return(temp);
        }
        for (let chars of zeusArr()) {
          for (let [key, value] of Object.entries(decryption_key)) {
            if (chars === key) {
              decrypting.push(value);
              encrypting.push(chars);
            }
          }
        }
        this.allowMetadata ? Encrypto.metadata = { ...metadata } : null;
        this.allowMetadata ? Encrypto.metadata.encryption_time = Date() : null;
        if (this.allPackages) {
          Encrypto.data.encrypt = encrypting.join(String());
          Encrypto.data.decrypt = decrypting.join(String());
          return(Encrypto);
        }
        this.decrypt ? Encrypto.data = decrypting.join(String()) : null;
        return(Encrypto);
      } catch (err_exception) {
        return ({ EXCEPTION: err_exception });
      }
    } else if (!this.encrypt && !this.decrypt) {
      return ({ error: "ERROR: Illegal operation - no method supplied" });
    } else {
      return ({ error: "ERROR: Can not perform two operations at once" });
    }
  }
}
 //Expected Object Format for ZeusEncrypt 

const testObj = {
  Data: "This is an instance",
  Decrypt: false,
  Encrypt: true,
  AllowMetadata: true,
  AllPackages: true
}
//new Zeus({ ...testObj })

const Zeus = ZeusEncryptZ8Engine
console.log(new Zeus({ ...testObj }))