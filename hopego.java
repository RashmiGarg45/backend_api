import java.nio.charset.StandardCharsets;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.ByteArrayOutputStream;
import java.util.zip.Deflater;
import java.util.zip.Inflater;

public class hopego {

    static final String AES_ALGORITHM = "AES/CBC/PKCS5Padding";
    static final String AES_NAME = "AES";
    static final int OFFSET = 16;
    static final String SECRET_KEY = "sgt$%@CVBGgdt12q";  // Must be 16 bytes
    static final byte[] KEY_BYTES = SECRET_KEY.getBytes(StandardCharsets.UTF_8);

    // Compress
    public static byte[] compress(String str) {
        try {
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
	        Deflater deflater = new Deflater(1);
	        deflater.setInput(str.getBytes(StandardCharsets.UTF_8));
	        deflater.finish();
	        byte[] bArr = new byte[4096];
	        while (!deflater.finished()) {
	            byteArrayOutputStream.write(bArr, 0, deflater.deflate(bArr));
	        }
	        deflater.end();
	        return byteArrayOutputStream.toByteArray();
	    }
        catch (Exception e) {
            throw new RuntimeException("Compression failed", e);
        }
    }

    // Decompress
    public static String decompress(byte[] compressed) {
    try {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        Inflater inflater = new Inflater();
        inflater.setInput(compressed);
        byte[] buffer = new byte[4096];
        while (!inflater.finished()) {
            int count = inflater.inflate(buffer);
            byteArrayOutputStream.write(buffer, 0, count);
        }
        inflater.end();
        return byteArrayOutputStream.toString(StandardCharsets.UTF_8.name());
    } catch (Exception e) {
        throw new RuntimeException("Decompression failed", e);
    }
}


    // Encryption
    public static byte[] encrypt(byte[] bArr) {
        try {
        return getCipher(SECRET_KEY.getBytes(StandardCharsets.UTF_8), 1).doFinal(bArr);
    } catch (Exception e) {
            throw new RuntimeException("Cipher failed", e);
        }
    }
    
    public static byte[] decrypt(byte[] bArr, byte[] bArr2) {
        try {
        return getCipher(bArr2, 2).doFinal(bArr);
        } catch (Exception e) {
            throw new RuntimeException("Cipher failed", e);
        }
    }

    // Decryption
    public static byte[] decrypt(byte[] bArr) {
        return decrypt(bArr, SECRET_KEY.getBytes(StandardCharsets.UTF_8));
    }

    // Core Cipher Logic
    public static Cipher getCipher(byte[] bArr, int i5) {
        try {
            SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, AES_NAME);
        IvParameterSpec ivParameterSpec = new IvParameterSpec(bArr, 0, 16);
        Cipher instance = Cipher.getInstance(AES_ALGORITHM);
        instance.init(i5, secretKeySpec, ivParameterSpec);
        return instance;
        
        } catch (Exception e) {
            throw new RuntimeException("Cipher failed", e);
        }
    }

    // Send (Compress + Encrypt)
    public static String send(String jsonData) {
        try {
            byte[] compressed = compress(jsonData);
            byte[] encrypted = encrypt(compressed);
            return new String(encrypted, StandardCharsets.ISO_8859_1); // Binary-safe encoding
        } catch (Exception e) {
            return null;
        }
    }

    // Receive (Decrypt + Decompress)
    public static String receive(String encryptedStr) {
        try {
            byte[] encryptedBytes = encryptedStr.getBytes(StandardCharsets.ISO_8859_1);
            byte[] decrypted = decrypt(encryptedBytes);
            return decompress(decrypted);
        } catch (Exception e) {
            throw new RuntimeException("Receive failed", e);
        }
    }

    public static void main(String[] args) {
        String originalJson = args[0];

        // Encrypt + Send
        String encryptedStr = send(originalJson);
        System.out.println("Encrypted string (ISO-8859-1): " + encryptedStr);
        
        // System.out.println("Encrypted string UTF-8): " + encryptedStr.getBytes(StandardCharsets.UTF_8));
        
        // byte[] encrypted = encryptedStr.getBytes(StandardCharsets.UTF_8);

        // Decrypt + Receive
        // String decryptedJson = receive(encryptedStr);
        // System.out.println("Decrypted string: " + decryptedJson);
    }
}
