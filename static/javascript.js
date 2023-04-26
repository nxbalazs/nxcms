var footer = document.querySelector('.footer');
if (document.documentElement.scrollHeight > window.innerHeight) {
    footer.classList.remove('fixed-position');
} else {
    footer.classList.add('fixed-position');
}


const tabButtons = document.querySelectorAll('.tab-button');
const tabPanels = document.querySelectorAll('.tab-panel');

function showPanel(panelIndex, colorCode) {
  tabButtons.forEach((button) => button.classList.remove('active'));
  tabButtons[panelIndex].classList.add('active');
  tabPanels.forEach((panel) => panel.classList.remove('active'));
  tabPanels[panelIndex].classList.add('active');
}

showPanel(0);

tabButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    showPanel(index);
  });
});