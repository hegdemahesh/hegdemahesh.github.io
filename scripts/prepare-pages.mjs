import { cp, mkdir, rm, writeFile, copyFile } from 'node:fs/promises';
import path from 'node:path';

const rootDir = process.cwd();
const distDir = path.join(rootDir, 'dist');
const docsDir = path.join(rootDir, 'docs');

await rm(docsDir, { recursive: true, force: true });
await mkdir(docsDir, { recursive: true });
await cp(distDir, docsDir, { recursive: true });
await copyFile(path.join(distDir, 'index.html'), path.join(docsDir, '404.html'));
await writeFile(path.join(docsDir, '.nojekyll'), '');