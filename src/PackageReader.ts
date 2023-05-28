import { BinaryReader } from 'google-protobuf';
import { Socket } from 'net';

class PackageReader {
    private buffer = Buffer.alloc(1024 * 1024);

    constructor{
        private socket: Socket;

    }
}