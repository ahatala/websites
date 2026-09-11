'use strict';
// The menus and recipes are static. Only checklists and family notes need JS.
const storage = {
  get(key) { try { return localStorage.getItem('festival:v2:' + key); } catch { return null; } },
  set(key, value) { try { localStorage.setItem('festival:v2:' + key, value); return true; } catch { return false; } }
};
document.querySelectorAll('[data-print]').forEach(button => button.addEventListener('click', () => window.print()));
document.querySelectorAll('[data-save]').forEach(input => {
  input.value = storage.get(input.dataset.save) || '';
  input.addEventListener('input', () => storage.set(input.dataset.save, input.value));
});
const checks = [...document.querySelectorAll('[data-shop]')];
const status = document.getElementById('status');
function updateProgress() {
  const progress = document.getElementById('progress');
  if (progress) progress.textContent = `${checks.filter(input => input.checked).length} of ${checks.length} checked`;
  checks.forEach(input => input.closest('.shop-item').classList.toggle('checked', input.checked));
}
checks.forEach(input => {
  input.checked = storage.get(input.dataset.shop) === 'true';
  input.addEventListener('change', () => {
    if (!storage.set(input.dataset.shop, String(input.checked)) && status) status.textContent = 'Browser storage is unavailable; ticks will last only on this page.';
    updateProgress();
  });
});
updateProgress();
document.getElementById('reset-list')?.addEventListener('click', () => {
  checks.forEach(input => { input.checked = false; storage.set(input.dataset.shop, 'false'); });
  updateProgress();
  status.textContent = 'This week’s ticks have been cleared.';
});
document.getElementById('copy-list')?.addEventListener('click', async () => {
  const text = document.getElementById('copy-text');
  try {
    await navigator.clipboard.writeText(text.value);
    status.textContent = 'Shopping list copied.';
  } catch {
    document.getElementById('copy-fallback').hidden = false;
    text.focus(); text.select();
    status.textContent = 'Select and copy the text below.';
  }
});
