import { createConnection, Socket } from 'net'

export class ReactOBS {
	static connect(host: string, port: number) {
		const socket: Socket = createConnection({ host, port }, async () => { })
		return new ReactOBS();
	}

	//constructor(api: ServerAPI) { }
}