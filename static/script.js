async function loadSummary() {
  const res = await fetch("/api/summary");
  const data = await res.json();

  document.getElementById("balance").textContent = "$" + data.balance.toFixed(2);
  document.getElementById("income").textContent = "$" + data.income.toFixed(2);
  document.getElementById("expenses").textContent = "$" + data.expenses.toFixed(2);

  const maxVal = Math.max(...Object.values(data.summary));
  const bars = document.getElementById("category-bars");
  bars.innerHTML = "";
  for (const [cat, total] of Object.entries(data.summary)) {
    const pct = maxVal > 0 ? (total / maxVal) * 100 : 0;
    bars.innerHTML += `
      <div class="bar-row">
        <div class="bar-label">${cat}</div>
        <div class="bar-track">
          <div class="bar-fill" style="width: ${pct}%"></div>
        </div>
        <div class="bar-val">$${total.toFixed(2)}</div>
      </div>`;
  }

  const txList = document.getElementById("recent-transactions");
  txList.innerHTML = "";
  if (data.transactions.length === 0) {
    txList.innerHTML = `<div style="font-size:13px; color:#aaa;">No transactions yet</div>`;
  } else {
    for (const t of data.transactions) {
      const sign = t.type === "income" ? "+" : "-";
      txList.innerHTML += `
        <div class="tx-row">
          <div>
            <div class="tx-name">${t.category}</div>
            <div class="tx-cat">${t.description || t.type}</div>
          </div>
          <span class="badge ${t.type}">${sign}$${t.amount.toFixed(2)}</span>
        </div>`;
    }
  }
}

async function addTransaction() {
  const amount = document.getElementById("amount").value;
  const category = document.getElementById("category").value;
  const type = document.getElementById("type").value;
  const description = document.getElementById("description").value;

  if (!amount || !category) {
    document.getElementById("add-msg").textContent = "Please fill in amount and category.";
    document.getElementById("add-msg").style.color = "#993C1D";
    return;
  }

  await fetch("/api/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, category, type, description })
  });

  document.getElementById("amount").value = "";
  document.getElementById("category").value = "";
  document.getElementById("description").value = "";
  document.getElementById("add-msg").textContent = "Transaction added!";
  document.getElementById("add-msg").style.color = "#0F6E56";

  setTimeout(() => {
    document.getElementById("add-msg").textContent = "";
  }, 2000);

  loadSummary();
}

async function calcTax() {
  const income = document.getElementById("tax-income").value;
  if (!income) return;

  const res = await fetch("/api/tax", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ income })
  });
  const d = await res.json();

  document.getElementById("tax-result").innerHTML = `
    <div style="margin-top: 1rem;">
      <div class="tax-result-row"><span>Gross income</span><span>$${d.gross.toLocaleString()}</span></div>
      <div class="tax-result-row"><span>Federal tax</span><span>$${d.federal_tax.toLocaleString()}</span></div>
      <div class="tax-result-row"><span>Ontario tax</span><span>$${d.ontario_tax.toLocaleString()}</span></div>
      <div class="tax-result-row"><span>Total tax</span><span>$${d.total_tax.toLocaleString()}</span></div>
      <div class="tax-result-row"><span>Effective rate</span><span>${d.effective_rate}%</span></div>
      <div class="tax-result-row total"><span>After-tax income</span><span>$${d.after_tax.toLocaleString()}</span></div>
    </div>`;
}

async function calcHst() {
  const amount = document.getElementById("hst-amount").value;
  if (!amount) return;

  const res = await fetch("/api/hst", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount })
  });
  const d = await res.json();

  document.getElementById("hst-result").innerHTML = `
    <div style="margin-top: 1rem;">
      <div class="tax-result-row"><span>Pre-tax amount</span><span>$${d.pre_tax.toFixed(2)}</span></div>
      <div class="tax-result-row"><span>HST (13%)</span><span>$${d.hst.toFixed(2)}</span></div>
      <div class="tax-result-row total"><span>Total</span><span>$${d.total.toFixed(2)}</span></div>
    </div>`;
}

function showPage(page) {
  document.getElementById("page-dashboard").style.display = page === "dashboard" ? "block" : "none";
  document.getElementById("page-tax").style.display = page === "tax" ? "block" : "none";

  document.querySelectorAll(".nav-item").forEach(el => el.classList.remove("active"));
  event.target.classList.add("active");
}

loadSummary();
