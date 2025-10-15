// KDP DESIGN - Single-file React component (Tailwind CSS)
// Usage:
// - Put this file in a React app (e.g., create-react-app, Vite, Next.js page).
// - Tailwind classes are used; ensure Tailwind is configured in your project.
// - Replace placeholder images (assets/*) and logo.png with your own files.
// - Contact form uses mailto by default; replace with Formspree or your backend endpoint if needed.

import React from 'react';

export default function KDPDesignSite(){
  return (
    <div className="min-h-screen bg-black text-[#d4af37] antialiased">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-black/95 backdrop-blur-md border-b border-black/40">
        <div className="max-w-6xl mx-auto flex items-center justify-between px-6 py-4">
          <div className="flex items-center gap-4">
            <img src="/assets/kdp-logo.png" alt="KDP DESIGN" className="h-12 w-auto object-contain" />
            <span className="text-xl font-semibold tracking-widest">KDP DESIGN</span>
          </div>

          <nav className="hidden md:flex items-center gap-6 text-sm">
            <a href="#accueil" className="hover:underline">Accueil</a>
            <a href="#galerie" className="hover:underline">Galerie</a>
            <a href="#services" className="hover:underline">Services</a>
            <a href="#a-propos" className="hover:underline">À propos</a>
            <a href="#contact" className="ml-2 px-4 py-2 rounded-full bg-[#d4af37] text-black font-semibold">Me contacter</a>
          </nav>

          <button id="mobile-menu-btn" className="md:hidden p-2 rounded-md focus:outline-none">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="#d4af37">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

        {/* Mobile menu (hidden by default) */}
        <div id="mobile-menu" className="md:hidden hidden px-6 pb-6">
          <div className="flex flex-col gap-4">
            <a href="#accueil" className="block">Accueil</a>
            <a href="#galerie" className="block">Galerie</a>
            <a href="#services" className="block">Services</a>
            <a href="#a-propos" className="block">À propos</a>
            <a href="#contact" className="block px-4 py-2 rounded-full bg-[#d4af37] text-black text-center">Me contacter</a>
          </div>
        </div>
      </header>

      {/* Main */}
      <main className="max-w-6xl mx-auto px-6 py-12">
        {/* Hero */}
        <section id="accueil" className="grid md:grid-cols-2 gap-8 items-center">
          <div>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight">KDP DESIGN</h2>
            <p className="mt-4 text-lg text-[#e9d999] max-w-xl">Photographie • Branding • Design visuel haut de gamme — L'art de capturer la perfection. Je capture votre histoire et crée des visuels qui parlent.</p>
            <div className="mt-6 flex gap-4">
              <a href="#contact" className="inline-block bg-[#d4af37] text-black px-6 py-3 rounded-full font-semibold">Me contacter</a>
              <a href="#galerie" className="inline-block border border-[#d4af37] px-6 py-3 rounded-full">Voir la galerie</a>
            </div>

            <div className="mt-8 text-sm text-gray-300">
              <strong>Basé à Touba & disponible partout au Sénégal.</strong>
            </div>
          </div>

          <div className="rounded-md overflow-hidden shadow-lg">
            <img src="/assets/hero.jpg" alt="Photo KDP DESIGN" className="w-full h-72 object-cover" />
          </div>
        </section>

        {/* Galerie / Portfolios */}
        <section id="galerie" className="mt-14">
          <h3 className="text-2xl font-semibold">Galerie — Sélection</h3>
          <p className="mt-2 text-sm text-gray-300 max-w-xl">Quelques projets récents (cliquez pour agrandir). Remplace ces images par les tiennes.</p>

          <div className="mt-6 grid grid-cols-2 md:grid-cols-3 gap-4">
            {/* Use your real images */}
            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/portfolio-portrait-red.jpg" alt="Projet 1" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
              <div className="absolute inset-0 bg-black/25 opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                <div className="text-sm">Portrait — Client A</div>
              </div>
            </div>

            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/portfolio-action-phone.jpg" alt="Projet 2" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
            </div>

            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/portfolio-event.jpg" alt="Projet 3" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
            </div>

            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/portfolio-studio.jpg" alt="Projet 4" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
            </div>

            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/portrait-smile.jpg" alt="Projet 5" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
            </div>

            <div className="group relative overflow-hidden rounded-md">
              <img src="/assets/night-blue1.jpg" alt="Projet 6" className="w-full h-48 object-cover group-hover:scale-105 transition-transform" />
            </div>
          </div>
        </section>

        {/* Services */}
        <section id="services" className="mt-14">
          <h3 className="text-2xl font-semibold">Services</h3>
          <p className="mt-2 text-sm text-gray-300 max-w-xl">Offres sur mesure pour particuliers et entreprises.</p>

          <div className="mt-6 grid md:grid-cols-3 gap-6">
            <div className="p-6 bg-black/60 rounded-lg border border-black/30">
              <h4 className="font-semibold">Photographie Portrait</h4>
              <p className="mt-2 text-sm text-gray-300">Séance en studio ou extérieur, retouches incluses.</p>
              <div className="mt-4 text-sm">À partir de 25 000 XOF</div>
            </div>

            <div className="p-6 bg-black/60 rounded-lg border border-black/30">
              <h4 className="font-semibold">Packshot & Produit</h4>
              <p className="mt-2 text-sm text-gray-300">Photos packshot pour e‑commerce et catalogues.</p>
              <div className="mt-4 text-sm">Tarifs sur demande</div>
            </div>

            <div className="p-6 bg-black/60 rounded-lg border border-black/30">
              <h4 className="font-semibold">Branding & Design</h4>
              <p className="mt-2 text-sm text-gray-300">Logo, identités visuelles, supports imprimés.</p>
              <div className="mt-4 text-sm">Forfaits disponibles</div>
            </div>
          </div>
        </section>

        {/* À propos */}
        <section id="a-propos" className="mt-14">
          <h3 className="text-2xl font-semibold">À propos</h3>
          <div className="mt-4 md:flex gap-6 items-center">
            <img src="/assets/about.jpg" alt="Oumar" className="w-48 h-48 object-cover rounded-md" />
            <div className="mt-4 md:mt-0">
              <p className="text-sm text-gray-300 max-w-xl">Je m'appelle <strong>Oumar Diallo</strong>. Photographe & designer graphique basé à Touba. J'aide les marques et particuliers à raconter leurs histoires par l'image, avec une approche soignée et professionnelle.</p>
              <ul className="mt-4 text-sm text-gray-300 space-y-2">
                <li>• 5+ ans d'expérience en photographie commerciale</li>
                <li>• Collaboration avec marques locales</li>
                <li>• Retouches avancées & gestion couleur</li>
              </ul>
            </div>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="mt-14 mb-20">
          <h3 className="text-2xl font-semibold">Contact & Réservation</h3>
          <p className="mt-2 text-sm text-gray-300 max-w-xl">Prêt à travailler ensemble ? Envoie un message ou réserve une séance.</p>

          <div className="mt-6 grid md:grid-cols-2 gap-6">
            <form className="bg-black/60 p-6 rounded-lg border border-black/30" action={`mailto:kadiallopord@gmail.com`} method="post" encType="text/plain">
              <label className="block text-sm text-gray-300">Nom
                <input name="name" className="w-full mt-2 p-2 rounded-md bg-black/80 border border-black/40 text-white" required />
              </label>

              <label className="block text-sm text-gray-300 mt-4">Email
                <input type="email" name="email" className="w-full mt-2 p-2 rounded-md bg-black/80 border border-black/40 text-white" required />
              </label>

              <label className="block text-sm text-gray-300 mt-4">Service
                <select name="service" className="w-full mt-2 p-2 rounded-md bg-black/80 border border-black/40 text-white">
                  <option>Photographie</option>
                  <option>Design & Branding</option>
                  <option>Packshot produit</option>
                </select>
              </label>

              <label className="block text-sm text-gray-300 mt-4">Message
                <textarea name="message" rows={4} className="w-full mt-2 p-2 rounded-md bg-black/80 border border-black/40 text-white" />
              </label>

              <div className="mt-4">
                <button type="submit" className="px-6 py-2 rounded-full bg-[#d4af37] text-black font-semibold">Envoyer</button>
              </div>
            </form>

            <div className="p-6 rounded-lg border border-black/30">
              <h4 className="font-semibold">Infos</h4>
              <p className="mt-2 text-sm text-gray-300">Email : <a href="mailto:kadiallopord@gmail.com" className="text-[#d4af37]">kadiallopord@gmail.com</a></p>
              <p className="mt-1 text-sm text-gray-300">Téléphone : +221785856138</p>
              <p className="mt-4 text-sm text-gray-300">Réseaux : Instagram / Facebook / WhatsApp</p>

              <div className="mt-6">
                <strong className="text-sm">Localisation</strong>
                <p className="text-sm text-gray-300">Touba, Sénégal</p>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-black/30 bg-black/95">
        <div className="max-w-6xl mx-auto px-6 py-6 text-sm text-gray-300 flex flex-col md:flex-row items-center justify-between">
          <div>© {new Date().getFullYear()} KDP DESIGN — Tous droits réservés</div>
          <div className="mt-2 md:mt-0">Mentions légales • Politique de confidentialité</div>
        </div>
      </footer>

      {/* Small script for mobile menu toggle - include in your app or adapt as needed */}
      <script dangerouslySetInnerHTML={{__html:`
        (function(){
          const btn = document.getElementById('mobile-menu-btn');
          const menu = document.getElementById('mobile-menu');
          if(!btn || !menu) return;
          btn.addEventListener('click', ()=>{
            menu.classList.toggle('hidden');
          });
        })();
      `}} />
    </div>
  );
}
